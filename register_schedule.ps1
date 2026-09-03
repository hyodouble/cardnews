<#
Registers the daily 08:00 publish as a Windows scheduled task.

    powershell -ExecutionPolicy Bypass -File register_schedule.ps1
    powershell -ExecutionPolicy Bypass -File register_schedule.ps1 -Time 07:30
    powershell -ExecutionPolicy Bypass -File register_schedule.ps1 -Remove

The task runs publish_today.py from this folder, which publishes that day's
carousel if content/<date>.json and its ten slides exist, and does nothing at
all if they don't. So a day with nothing prepared costs one silent no-op.

The machine has to be awake at that hour. -WakeToRun is set, but it only wakes
a sleeping machine, never a machine that is shut down or unplugged. On a
weekend when the PC is off, prepare the carousel and publish from wherever you
are -- see SETUP.md.
#>
param(
    [string]$Time = "08:00",
    [switch]$Remove
)

$taskName = "cardnews-publish"
$repo = Split-Path -Parent $MyInvocation.MyCommand.Path

if ($Remove) {
    Unregister-ScheduledTask -TaskName $taskName -Confirm:$false
    "removed $taskName"
    exit
}

$python = (Get-Command python).Source
if (-not $python) { throw "python not found on PATH" }

$action = New-ScheduledTaskAction -Execute $python `
    -Argument "publish_today.py" -WorkingDirectory $repo
$trigger = New-ScheduledTaskTrigger -Daily -At $Time
$settings = New-ScheduledTaskSettingsSet -WakeToRun `
    -StartWhenAvailable -DontStopOnIdleEnd `
    -ExecutionTimeLimit (New-TimeSpan -Minutes 30)

Register-ScheduledTask -TaskName $taskName -Action $action -Trigger $trigger `
    -Settings $settings -Description "Publish the day's card news to Instagram, Facebook and Threads" `
    -Force | Out-Null

"registered $taskName at $Time daily"
"  python : $python"
"  folder : $repo"
"  test it: Start-ScheduledTask -TaskName $taskName   (publishes immediately)"
