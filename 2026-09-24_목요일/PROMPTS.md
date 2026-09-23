# Gemini 이미지 프롬프트 — 2026-09-24 (종량제 봉투)

10장 전부 아래 지시문으로 생성한다. `assets/2026-09-24/`에 이 파일명으로 넣는다.

`hook.png` `content2.png` `content3.png` `content4.png` `stat.png` `content6.png`
`content7.png` `content8.png` `content9.png` `cta.png`

계정은 `hoohihi123123`(Gemini Pro), 이미지 모드. 이 계정은 이 컴퓨터에서 `/u/2` 다.
`https://gemini.google.com/u/2/images` 로 새로 열면 새 채팅 + 이미지 모드가 한 번에 잡힌다.
**컷마다 새 채팅을 연다.** 같은 채팅에서 다음 프롬프트를 넣으면 생성이 아니라 편집으로 처리된다.

새 채팅을 연 직후 **첫 입력은 입력창에 들어가지 않는다.** 클릭하고 타이핑해도 빈 채로 남으므로,
화면을 확인하고 **한 번 더 타이핑해야** 글자가 들어간다.

## 공통 블록은 셋이다

`People appear only from behind` 류의 문구는 모델이 **사람을 넣으라는 지시로 읽는다.** 무인 컷에
인물 블록을 쓰면 배경에 사람이 깔리므로 컷 성격대로 나눠 쓴다. 이 편은 무인 컷이 대부분이다.

**손만** — `content2`, `content6`, `content7`

```
Photorealistic documentary photograph, square 1:1 framing, shot in a Korean apartment. Slight film grain.
Only hands and forearms enter the frame from the edges — no faces, no heads, no shoulders, no bodies, no
reflections of people. No text, no signage lettering, no Hangul, no letters, no numbers, no logos, no
watermarks.
```

**실외-무인용** — `hook`, `content3`, `content4`, `stat`, `content8`, `content9`, `cta`

```
Photorealistic documentary photograph, square 1:1 framing, shot outdoors in a Korean residential
neighbourhood. Slight film grain. No people anywhere in the frame, no hands, no faces, no bodies, no
silhouettes. The subject sits in the upper two-thirds; the bottom third is calm and uncluttered so text can
sit over it. No text, no signage lettering, no Hangul, no letters, no numbers, no logos, no watermarks.
```

## 다운로드는 1024로 줄여서 저장한다

Gemini의 '원본 크기 다운로드'는 **2048x2048**을 준다. `make_cards.py`의 워터마크 트림은
`img.size == (1024, 1024)`일 때만 동작하므로, 2048 그대로 넣으면 **✦ 워터마크가 카드에 그대로 남는다.**

```bash
python grab.py 2026-09-24 hook
```

`grab.py`가 `~/Downloads`의 최신 Gemini 파일을 1024로 줄여 `assets/<날짜>/`에 넣고 원본을 지운다.
3분보다 오래된 파일은 거부한다.

**다운로드 버튼은 이미지 오른쪽 위 세 아이콘 중 맨 오른쪽이다.** 왼쪽은 공유(공개 링크 생성),
가운데는 클립보드 복사다.

## 이 편에서 그림이 깨지는 지점 다섯

- **봉투에 글자가 박힌다.** 제일 크게 걸리는 지점이다. 실제 종량제 봉투는 구 이름과 용량이 크게
  인쇄돼 있어서 모델이 글자를 넣으려 한다. 모든 컷에 `completely plain, unprinted` 를 넣었다.
  글자·숫자·로고가 보이면 재생성이다.

- **봉투 색이 검정 쓰레기봉투로 나온다.** 한국 종량제 봉투는 **반투명한 얇은 비닐**이고 색은
  흰색·연한 주황·연두 계열이다. 두꺼운 검정 봉투, 미국식 대형 초록 봉투가 나오면 틀렸다.
  이 편은 **반투명 연한 주황**으로 통일했다.

- **분리수거장이 미국식 대형 컨테이너로 나온다.** 한국 아파트 분리수거장은 **낮은 지붕 아래
  색깔만 다른 커다란 자루·플라스틱 통이 한 줄로 선 곳**이다. 초록·파랑 바퀴 달린 대형 쓰레기
  컨테이너(dumpster)가 보이면 틀렸다.

- **음식물 수거함이 일반 쓰레기통으로 나온다.** `content6`은 **허리 높이의 네모난 회색 통,
  윗면에 작은 카드 대는 판과 손잡이 달린 뚜껑** 하나다. 화면·숫자 표시창에 글자가 들어가면 틀렸다.

- **stat 컷에 숫자가 새겨진다.** 1995는 카드 글자로 들어간다. 사진에는 **봉투 한 줄**만 둔다 —
  달력, 영수증, 가격표를 절대 넣지 말 것. 재생성할 때도 다시 집어넣지 말 것.

---

아래가 장면 지시문이다. 재생성할 때는 해당 공통 블록을 이어 붙인다.

## hook.png — 골목에 내놓은 봉투들 (실외-무인 블록)

봉투 단위로 돈을 낸다는 걸 한 장으로 세우는 컷이다. **똑같은 봉투가 줄지어 선 것**이 훅이다.

```
A row of five tied, bulging, translucent pale orange plastic trash bags set out against a low wall on a
narrow Korean residential street at dusk, all the same size and colour, completely plain and unprinted.
A street lamp glows above, low brick villa buildings behind. No black bags, no dumpsters, no loose trash
on the ground. No people anywhere, no hands. The lower third of the frame is empty dark pavement.
```

## content2.png — 봉투 한 묶음을 드는 손 (손만 블록)

이름을 설명하는 장이다. **새로 산 접힌 봉투 묶음**이 또렷하게 읽혀야 한다.

```
Close view of two hands holding a small bundle of ten new, neatly folded translucent pale orange plastic
trash bags held together with a thin paper band, completely plain and unprinted, just bought. Plain light
kitchen counter in the background, softly blurred. No receipts, no shop, no packaging, no labels, no
lettering on the bags or the band. Only hands and forearms enter the frame, no faces, no heads, no
shoulders. Warm indoor light. The lower third of the frame is plain counter surface.
```

## content3.png — 동네 경계의 두 골목 (실외-무인 블록)

구마다 봉투가 다르다는 장이다. 사람 없이 **서로 다른 색의 봉투 두 줄**로 말한다.

```
A quiet Korean residential street corner in the early evening, two small groups of tied translucent trash
bags set out on either side of the corner: pale orange bags on the left, pale green bags on the right,
completely plain and unprinted. Low villa buildings, a utility pole, a few parked scooters. No people
anywhere, no hands, no black bags, no dumpsters. Every sign and wall surface is blank. The lower third of
the frame is empty pavement.
```

## content4.png — 아파트 분리수거장 (실외-무인 블록)

재활용은 공짜지만 분리해야 한다는 장이다. **낮은 지붕 아래 한 줄로 선 자루와 통**이어야 한다.

```
The recycling area of a Korean apartment complex under a low metal roof: a row of large woven sacks and
plastic bins in different colours standing side by side, one holding crushed plastic bottles, one holding
flattened cardboard, one holding aluminium cans, one holding white styrofoam blocks, one holding glass
bottles. Clean paved ground, apartment towers in the background at dusk. No dumpsters, no wheelie bins.
Every sign and bin surface is completely blank. No people anywhere, no hands. The lower third of the frame
is clean empty pavement.
```

## stat.png — 봉투 한 줄 (실외-무인 블록)

1995년에 봉투 단위 과금이 시작됐다는 장이다. 숫자는 카드가 말하고 **사진은 봉투 한 줄**만 둔다.

```
A single tied, full, translucent pale orange plastic trash bag standing alone at the foot of a plain grey
concrete wall on a quiet Korean street at night, lit from one side by a street lamp, completely plain and
unprinted. Nothing else in frame but the wall and the pavement. No calendars, no receipts, no price tags,
no numbers, no black bags. No people anywhere, no hands. The lower third of the frame is dark empty
pavement.
```

## content6.png — 음식물 수거함에 카드 대는 손 (손만 블록)

음식물이 무게로 과금된다는 장이다. **통 윗면의 카드 판과 손 하나**면 된다.

```
Close view of a waist-high square grey food waste collection bin outside a Korean apartment building, a
hand holding a small plain white plastic card against a flat reader panel on its top beside a handled lid.
The panel's small display is dark and blank. Evening light, apartment entrance softly blurred behind. No
screens showing text or numbers, no labels, no logos, no lettering anywhere on the bin. Only hands and
forearms enter the frame, no faces, no heads, no shoulders. The lower third of the frame is the plain
front of the bin.
```

## content7.png — 치킨 뼈를 봉투에 넣는 손 (손만 블록)

뼈는 음식물이 아니라는 장이다. **닭뼈가 음식물 통이 아니라 봉투로** 들어가는 동작이 보여야 한다.

```
Overhead view of a Korean kitchen counter: a hand tipping leftover fried chicken bones from a plain
cardboard tray into an open translucent pale orange plastic trash bag, completely plain and unprinted. Beside
it a small closed plastic food waste caddy and a few eggshells on a plate. No brand boxes, no logos, no
labels, no lettering on anything. Only hands and forearms enter the frame, no faces, no heads, no
shoulders. Warm indoor light. The lower third of the frame is bare counter surface.
```

## content8.png — 골목에 남겨진 검은 봉투 (실외-무인 블록)

잘못된 봉투는 수거되지 않는다는 장이다. **깨끗이 치워진 자리 옆에 혼자 남은 봉투 하나**로 말한다.

```
A narrow Korean residential alley in the early morning after collection: the pavement is swept clean except
for one plain black plastic bag left alone beside a utility pole, a small security camera mounted high on
the pole pointing down at it. Low brick villa buildings on both sides. No other bags, no dumpsters. Every
sign and wall surface is completely blank, no warning notices. No people anywhere, no hands. The lower
third of the frame is clean empty pavement.
```

## content9.png — 수거일 밤의 아파트 입구 (실외-무인 블록)

정리 장이다. **내놓은 봉투와 분리된 박스가 가지런한 수거일 밤**으로 말한다.

```
The entrance of a small Korean apartment building on collection night: two tied translucent pale orange
trash bags, completely plain and unprinted, and a neat stack of flattened cardboard tied with string, set
side by side beside the door. Warm light from the lobby glass door, a row of bicycles along the wall. No
black bags, no dumpsters. Every sign is a completely blank surface. No people anywhere, no hands, no
figures behind the glass. The lower third of the frame is empty paving.
```

## cta.png — 새벽 골목 (실외-무인 블록)

계정 마무리 컷이다. 수거가 끝난 깨끗한 골목으로 조용하게 끝낸다.

```
A quiet Korean residential alley at dawn after the trash has been collected, the pavement clean and
slightly wet, low villa buildings with small balconies on both sides, a pale blue sky over the rooftops and
a single street lamp still on. No bags, no trash, no dumpsters. Every sign and wall surface is completely
blank with no writing, numbers or symbols. No people anywhere, no figures in windows. The lower third of the
frame is empty wet pavement.
```
