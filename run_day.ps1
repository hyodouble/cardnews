<#
Render, push and publish one day's carousel in a single run.

    powershell -ExecutionPolicy Bypass -File run_day.ps1
    powershell -ExecutionPolicy Bypass -File run_day.ps1 -Date 2026-09-14
    powershell -ExecutionPolicy Bypass -File run_day.ps1 -Yes          # no confirmation
    powershell -ExecutionPolicy Bypass -File run_day.ps1 -RenderOnly   # stop before posting

What it does, in order: pull, render the ten slides into img/<date> and into the
desktop day folder, write the brief, commit and push the slides, wait until
GitHub Pages actually serves the first one, then publish.

The wait matters. post.py HEADs every slide URL and refuses to run if one is not
public yet, and Pages takes about a minute to deploy after a push.

Publishing still asks before it posts, because that is the one step this repo
deliberately keeps manual -- see README. -Yes skips the question, -RenderOnly
stops after the push and leaves the posting for later.
#>
param(
    [string]$Date = (Get-Date -Format 'yyyy-MM-dd'),
    [switch]$Yes,
    [switch]$RenderOnly
)

$ErrorActionPreference = "Stop"
# PowerShell 7.4 turns a non-zero exit from git or python into a thrown error,
# which would jump past every $LASTEXITCODE check below -- including the one on
# "git diff --cached --quiet", whose exit 1 just means "there are staged changes".
if (Test-Path variable:PSNativeCommandUseErrorActionPreference) {
    $PSNativeCommandUseErrorActionPreference = $false
}
$repo = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $repo

function Fail($message) { Write-Host "STOP: $message" -ForegroundColor Red; exit 1 }
function Step($message) { Write-Host "`n== $message" -ForegroundColor Cyan }

$content = "content/$Date.json"
if (-not (Test-Path $content)) { Fail "no $content -- nothing prepared for $Date" }

$photos = Get-ChildItem "assets/$Date" -Filter *.png -ErrorAction SilentlyContinue
if ($photos.Count -lt 10) { Fail "assets/$Date has $($photos.Count) photos, needs 10" }

$day = Get-Content $content -Raw -Encoding UTF8 | ConvertFrom-Json
$folder = Join-Path ([Environment]::GetFolderPath('Desktop')) "$Date`_$($day.weekday)"
Write-Host "$Date ($($day.weekday)) -- $($day.title)"

Step "pulling"
git pull --ff-only
if ($LASTEXITCODE -ne 0) { Fail "git pull failed -- resolve it by hand, then run this again" }

Step "rendering"
python make_cards.py $content "img/$Date" (Join-Path $folder "slides")
if ($LASTEXITCODE -ne 0) { Fail "make_cards.py failed" }
python make_brief.py $content $folder
if ($LASTEXITCODE -ne 0) { Fail "make_brief.py failed" }

$slides = Get-ChildItem "img/$Date" -Filter *.png
if ($slides.Count -ne 10) { Fail "img/$Date has $($slides.Count) slides, needs 10" }
Write-Host "10 slides in img/$Date and in $folder"

Step "pushing"
git add "img/$Date" "assets/$Date" $content
git diff --cached --quiet
if ($LASTEXITCODE -ne 0) {
    git commit -m "Render the $Date slides"
    if ($LASTEXITCODE -ne 0) { Fail "git commit failed" }
}
git push
if ($LASTEXITCODE -ne 0) { Fail "git push failed -- the slides must be public before posting" }

Step "waiting for GitHub Pages"
$envLine = Select-String -Path ".env" -Pattern '^BASE_URL=(.+)$'
if (-not $envLine) { Fail "no BASE_URL in .env" }
$base = $envLine.Matches[0].Groups[1].Value.Trim()
$url = "$($base.TrimEnd('/'))/img/$Date/01.png"
$live = $false
foreach ($attempt in 1..20) {
    try {
        $code = (Invoke-WebRequest -Uri $url -Method Head -UseBasicParsing -TimeoutSec 10).StatusCode
        if ($code -eq 200) { $live = $true; break }
    } catch { }
    Write-Host "  not served yet ($attempt/20), waiting 15s"
    Start-Sleep -Seconds 15
}
if (-not $live) { Fail "$url still not public after five minutes -- check the Pages build, then run with -Date $Date again" }
Write-Host "serving $url"

if ($RenderOnly) {
    Write-Host "`nrendered and pushed. To post it:  python publish_today.py $Date"
    exit 0
}

Step "publishing"
if (-not $Yes) {
    $answer = Read-Host "Post '$($day.title)' to Instagram, Facebook and Threads? [y/N]"
    if ($answer -ne 'y') { Write-Host "left unpublished. To post it later:  python publish_today.py $Date"; exit 0 }
}
python publish_today.py $Date
$published = $LASTEXITCODE

Write-Host ""
if ($published -eq 0) {
    Write-Host "published. Mark the day in the README table." -ForegroundColor Green
} else {
    Write-Host "publish_today.py reported a failure. Read publish.log." -ForegroundColor Yellow
    Write-Host "Instagram can answer 403 and post anyway, so check before retrying:"
    Write-Host "  python -c ""import os,post; post.load_env(); ig=os.environ['IG_USER_ID']; print(post.call(f'{post.GRAPH}/{ig}/media',{'fields':'id,timestamp','limit':'3','access_token':os.environ['PAGE_TOKEN']},'GET'))"""
}
Write-Host "Facebook's first comment does not go up through the API. Paste the 'reply' from $content by hand."
