# Gemini 이미지 프롬프트 — 2026-09-17 (수능)

10장 전부 아래 지시문으로 생성한다. `assets/2026-09-17/`에 이 파일명으로 넣는다.

`hook.png` `content2.png` `content3.png` `content4.png` `stat.png` `content6.png`
`content7.png` `content8.png` `content9.png` `cta.png`

계정은 `hoohihi123123`(Gemini Pro), 이미지 모드(Nano Banana 2).
**컷마다 새 채팅을 연다.** 같은 채팅에서 다음 프롬프트를 넣으면 생성이 아니라 직전 이미지의
편집으로 처리된다. `https://gemini.google.com/u/1/images` 로 새로 열면 새 채팅 + 이미지 모드가
한 번에 잡힌다.

## 공통 블록은 다섯이다

2026-09-16 편에서 확인된 것: 공통 블록이 장면 지시문을 이긴다. 특히 블록의
`People appear only from behind` 는 모델이 **사람을 넣으라는 지시로 읽는다.** 그래서 무인 컷에
인물 블록을 쓰면 배경에 사람이 깔린다. 이 편은 무인 컷이 다섯이라 블록을 컷 성격대로 나눈다.

**실내-인물용** — `content2`

```
Photorealistic documentary photograph, square 1:1 framing, shot indoors in a Korean school. Slight film grain,
shallow depth of field. The subject sits in the upper two-thirds of the frame; the bottom third is calm and
uncluttered so text can sit over it. People appear only from behind, cropped at the shoulders, or blurred.
No text, no signage lettering, no Hangul, no letters, no numbers, no logos, no watermarks, no recognizable faces.
```

**실내-무인용** — `content3`, `content4`

```
Photorealistic documentary photograph, square 1:1 framing, shot indoors in Korea. Slight film grain, shallow
depth of field. No people anywhere in the frame, no hands, no faces, no bodies, no silhouettes. The subject
sits in the upper two-thirds; the bottom third is calm and uncluttered so text can sit over it. No text, no
signage lettering, no Hangul, no letters, no numbers, no logos, no watermarks.
```

**탑다운 무인용** — `content7`

```
Photorealistic documentary photograph, square 1:1 framing, shot indoors in Korea. Slight film grain. No people
anywhere in the frame, no hands, no faces, no bodies, no chairs, no room, no background, no window. No text,
no signage lettering, no Hangul, no letters, no numbers, no logos, no watermarks.
```

**실외-무인용** — `hook`, `stat`

```
Photorealistic documentary photograph, square 1:1 framing, shot outdoors in Korea on a clear late-autumn
morning. Slight film grain. No people anywhere in the frame, no hands, no faces, no bodies, no silhouettes.
No text, no signage lettering, no Hangul, no letters, no numbers, no logos, no watermarks.
```

**실외-인물용** — `content6`, `content8`, `content9`, `cta`

```
Photorealistic documentary photograph, square 1:1 framing, shot outdoors in Korea on an overcast late-autumn
day, cold light. Slight film grain, shallow depth of field. The subject sits in the upper two-thirds; the
bottom third is calm and uncluttered so text can sit over it. People appear only from behind, cropped at the
shoulders, or blurred. No text, no signage lettering, no Hangul, no letters, no numbers, no logos, no
watermarks, no recognizable faces.
```

`cta`는 인물이 없어도 이 블록을 쓴다 — 동네 묘사가 장면 지시문 안에 다 들어가 있고,
2026-09-16 편에서 이 조합으로 한 번에 나왔다.

## 다운로드는 1024로 줄여서 저장한다

Gemini의 '원본 크기 다운로드'는 **2048x2048**을 준다. `make_cards.py`의 워터마크 트림은
`img.size == (1024, 1024)`일 때만 동작하므로, 2048 그대로 넣으면 **✦ 워터마크가 카드에 그대로 남는다.**

```bash
sips -z 1024 1024 ~/Downloads/Gemini_Generated_Image_xxxx.png --out assets/2026-09-17/hook.png
```

다운로드가 파일로 떨어지기까지 클릭 후 8~15초가 걸린다. 그 전에 `~/Downloads` 를 훑으면
**직전 편의 남은 파일을 집어간다.** 최근 3분 안에 생성된 파일만 고르도록 막아 두고 쓸 것.

## 이 편에서 그림이 깨지는 지점 여덟

- **소재가 시험이라 모델이 글자를 그리고 싶어한다.** 시험지, 칠판, 현수막, 수험표, 순찰차 차체
  표기가 컷마다 나오는데 전부 글자 자리다. 공통 블록의 `no letters` 하나로는 진다 —
  **종이·화면·차체·간판이 나오는 컷은 컷마다 따로 '백지' 또는 '읽을 수 없게 블러'를 다시 박는다.**
  아래 지시문에 이미 들어가 있으니 재생성할 때 지우지 말 것.

- **한국 교실이 서양 교실로 나온다.** 서양 교실은 큰 공용 테이블에 카펫, 벽에 포스터가 가득이다.
  한국 시험장은 **1인용 나무 책상이 줄 맞춰 떨어져 놓이고, 천장은 형광등, 창에는 얇은 커튼,
  바닥은 비닐 타일**이다. `individual single-person wooden desks spaced apart in straight rows,
  fluorescent ceiling tubes, thin curtains, vinyl tile floor` 로 못 박는다.

- **수능날은 교복을 안 입는다.** 11월 중순이라 대부분 **사복에 검은 패딩**이다. 교복으로 그리면
  수능날이 아니라 그냥 학교다. `plain dark puffer jackets and casual clothes, not school uniforms` 를 붙인다.

- **순찰차가 미국 경찰차로 나온다.** 한국 순찰차는 **흰 차체에 파란 띠, 지붕에 낮고 넓은 경광등**이다.
  차체 표기를 지우면 경찰차로 안 읽히므로 **경광등을 식별 단서로 강조하고 표기는 백지**로 간다.
  `a white patrol sedan with a blue stripe along its side and a low wide light bar on the roof, every
  marking on the body left completely blank` 로 쓴다. 미국식 흑백 SUV가 나오면 틀린 것이다.

- **빈 하늘에 비행운이 생긴다.** `stat`과 `hook`의 요점은 **비행기가 없다**는 것이다. 모델은 하늘을
  그리라고 하면 비행운이나 점 하나를 넣는다. `no aircraft, no contrails, no vapour trails, no distant
  specks, completely empty sky` 를 두 컷 모두에 박는다.

- **활주로에 비행기가 돌아온다.** `hook`도 같은 문제다. 게이트에 세워 둔 기체까지 빼면 공항으로
  안 읽히므로, **움직이는 항공기 없음 + 활주로 위 완전 비움**으로 나눠서 지시한다.

- **사람을 넣으면 얼굴이 따라온다.** 교문 앞 학부모(`content9`)와 졸업식(`content6`)이 위험하다.
  두 컷 다 **뒤에서 찍거나 어깨에서 자른다**를 장면 지시문에 다시 쓴다. 그래도 얼굴이 들어오면
  재생성보다 **뒷모습만 남는 더 먼 구도로 바꾸는 편이 싸다**(2026-09-15 편에서 확인).

- **한국 졸업식 꽃다발은 종이로 감싼다.** 서양식 셀로판이나 리본 박스가 나오면 한국 장면이 아니다.
  `bouquets wrapped in plain matte paper` 를 붙인다.

---

아래가 장면 지시문이다. 재생성할 때는 해당 공통 블록을 이어 붙인다.

## hook.png — 텅 빈 활주로 (실외-무인 블록)

카드 문구가 "35분간 착륙하는 비행기가 없다"이다. 비어 있음 자체가 그림이라 활주로만 남긴다.

```
A long empty airport runway seen from an elevated position beside it, stretching away to the horizon under a
clear pale late-autumn sky. The runway surface is completely empty end to end: no aircraft taking off, no
aircraft landing, no aircraft rolling, nothing on the tarmac at all. The sky above is completely empty as
well, no aircraft, no contrails, no vapour trails, no distant specks. Flat dry grass on both sides of the
runway, low grey service buildings far away on the left, blurred past reading. All runway markings on the
tarmac are left completely blank with no numbers, letters or painted characters of any kind. Cold clear
morning light. The lower third of the frame is bare empty tarmac.
```

## content2.png — 시험장 교실 뒷줄에서 (실내-인물 블록)

"50만 명이 같은 날 아침"을 사람으로 그리되 얼굴을 없앤다. 교실 맨 뒤에서 찍는다.

```
A Korean exam-hall classroom shot from the very back of the room looking forward down the rows: individual
single-person wooden desks spaced apart in straight rows, a student seated at each one seen strictly from
behind and cropped at the shoulders so no face or head profile is visible, all in plain dark puffer jackets
and casual clothes, not school uniforms, all bent slightly forward over their desks. On each desk a sheet of
completely blank white paper and one pencil, no printing, no ruled lines, no boxes, no handwriting anywhere.
Fluorescent ceiling tubes, thin pale curtains half drawn over tall windows, vinyl tile floor, a blank
greenish chalkboard at the far end with nothing written on it. Cold even light, the lower third of the frame
is bare floor between the back desks.
```

## content3.png — 새벽 독서실 칸막이 책상 (실내-무인 블록)

"다음 기회는 12개월 뒤"를 재수의 자리로 그린다. 사람을 넣으면 얼굴이 따라오므로 비워 둔다.

```
A row of partitioned study carrels in a Korean reading room late at night, seen from a low angle down the
row: narrow wooden desks divided by tall panels on three sides, one small desk lamp switched on over a single
carrel in the middle of the row while every other carrel is dark, a chair pushed back and empty beneath it.
On the lit desk a stack of completely blank white paper and a closed plain notebook, no printing, no ruled
lines, no titles, no handwriting of any kind. The room is entirely empty of people. Deep shadow along the
row, warm pool of lamplight, the lower third of the frame is dark bare floor.
```

## content4.png — 10시까지 비어 있는 사무실 (실내-무인 블록)

증시와 관공서가 한 시간 늦게 여는 아침이다. 평소라면 차 있어야 할 자리가 비어 있는 게 요점이다.

```
An open-plan Korean office floor photographed in early morning daylight, completely empty of people: rows of
plain desks with dark monitors all switched off, office chairs pushed in at neat angles, a single grey coat
left over one chair back. Low partitions between the desks, pale floor tiles, tall windows along the far wall
with cold blue morning light coming through and blinds half raised. No one anywhere in the frame, no
silhouettes, no figures through the glass. Every screen is black and every surface is bare, with no printing,
labels or lettering on anything. The lower third of the frame is empty floor and chair legs.
```

## stat.png — 아무것도 없는 하늘 (실외-무인 블록)

35분간 닫힌 영공이다. 이 컷은 숫자 아래 깔리는 배경이므로 단순할수록 낫다.

```
Looking straight up at an empty late-autumn sky from ground level, the frame filled almost entirely by pale
cold blue sky with a few thin high clouds drifting across the upper half. The sky is completely empty: no
aircraft, no contrails, no vapour trails, no distant specks, no birds, nothing crossing it at all. Along the
very bottom edge, the dark out-of-focus tops of bare tree branches and one concrete rooftop parapet, in
shadow. The lower third of the frame is calm unbroken sky with nothing in it.
```

## content6.png — 졸업식 꽃다발 (실외-인물 블록)

"출신 대학이 평생 따라온다"를 학위복으로 그린다. 정문 간판을 넣으면 글자가 생기므로 뺀다.

```
A small group of people in black academic graduation gowns standing together on a university campus path,
all seen strictly from behind and cropped at the shoulders so no face is visible, each holding a bouquet
wrapped in plain matte paper down at their side. The gowns are plain black with no crests, no printed
lettering and no visible trim. A stone campus building stands blurred well behind them with all its signage
out of focus past reading. Bare autumn trees, overcast cold light. The lower third of the frame is empty
paving.
```

## content7.png — 밀봉된 시험지 봉투 하나 (탑다운 무인 블록)

다른 나라는 여러 학교 여러 번, 여기는 하루다. 그래서 딱 하나만 놓는다.
2026-09-16 편의 `stat`이 봉투 더미였으므로 이 컷은 정확히 그 반대로 간다.

```
Top-down overhead flat-lay: the camera is mounted directly above a desk pointing straight down at 90 degrees,
and the plain dark desk surface fills the entire frame edge to edge so nothing else is visible. Lying alone
at the centre of the desk, one single sealed manila document envelope, completely blank with no printing,
labels, stamps, barcodes or handwriting of any kind, its flap taped shut across the middle with one strip of
plain tape. Nothing else on the desk at all, no pens, no papers, no objects. Cool even light from above. The
lower third of the frame is bare empty desk surface.
```

## content8.png — 교문 앞 순찰차 (실외-인물 블록)

지각생을 태워다 주는 장면이다. 차체 표기를 지우면 경찰차로 안 읽히므로 경광등으로 식별시킨다.

```
A white patrol sedan with a blue stripe along its side and a low wide light bar on the roof, stopped at the
kerb directly in front of a Korean school's steel sliding gate with its rear door standing open. Every
marking on the car body, doors and number plate is left completely blank, no lettering, no numbers, no
emblems, no printing of any kind. One student in a plain dark puffer jacket is caught mid-stride running
from the car toward the gate, seen strictly from behind and cropped at the shoulders so no face is visible,
a plain bag in one hand. Concrete gate posts and a bare grey wall behind, no banners and no signs anywhere.
Cold overcast morning light. The lower third of the frame is empty road surface.
```

## content9.png — 닫힌 교문 밖에서 기다리는 사람들 (실외-인물 블록)

시험은 애들이 보고 나라가 밖에서 기다린다. 이 편에서 가장 중요한 컷이다.

```
A closed steel sliding school gate seen from the street side, with a loose group of adults standing and
waiting on the pavement in front of it, every one of them seen strictly from behind and cropped at the
shoulders so no face is visible, all in heavy dark winter coats, some with hands pressed together, standing
apart from one another rather than in a crowd. The gate is shut and the schoolyard beyond it is empty and
blurred. Bare concrete gate posts and a grey wall, no banners, no notices and no signs anywhere in the frame.
Cold flat overcast light, long shadows absent. The lower third of the frame is bare pavement.
```

## cta.png — 해질녘 동네 전경 (실외-인물 블록)

시리즈 공통 마무리 컷이다. 2026-09-16 편과 같은 구도로 간다.

```
A wide elevated view across a Korean residential district at dusk, looking down a long shallow valley of
rooftops: low-rise brick and beige-tiled buildings with stainless water tanks and air-conditioner units on
their flat roofs, tangled overhead cables strung between poles, slab apartment towers rising along both
sides with their windows lighting up one by one, low dark hills closing the skyline and a deep orange sky
above them. The lower third of the frame is quiet uncluttered rooftops in shadow.
```

---

## 손으로 돌릴 때 (2026-09-16 자동화 시도에서 확인된 것)

- **가로세로 비율 기본값이 16:9다.** 입력창 아래 칩에서 **컷마다 1:1로 바꾼다.** 새 채팅을 열면
  매번 초기화된다. 페이지는 정사각형 이미지도 가로로 잘라 보여주므로 화면만 보고 판단하지 말 것.
- 이미 만들어 둔 컷 둘 (다운로드만 하면 된다):
  - `hook` — https://gemini.google.com/u/2/app/b2799c4a1f59a175
  - `content2` — https://gemini.google.com/u/2/app/4a013c009c52defd
- 계정은 `/u/2/`다. 좌상단 인사가 "hihi님"이면 맞다.

10장을 **위 파일 순서대로** 내려받은 다음, 마지막에 한 번 돌린다:

```zsh
cd ~/cardnews && mkdir -p assets/2026-09-17
files=($(ls -tr ~/Downloads/Gemini_Generated_Image_*.png | tail -10))
names=(hook content2 content3 content4 stat content6 content7 content8 content9 cta)
[ ${#files} -eq 10 ] || echo "받은 파일이 ${#files}개다. 10개가 아니면 멈출 것."
for i in {1..10}; do sips -z 1024 1024 "${files[$i]}" --out "assets/2026-09-17/${names[$i]}.png"; done
ls assets/2026-09-17
```

순서가 어긋나면 `assets/2026-09-17`를 지우고 다시 받는 편이 빠르다. 다 넣었으면:

```bash
./run_day.sh 2026-09-17 --render-only
```
