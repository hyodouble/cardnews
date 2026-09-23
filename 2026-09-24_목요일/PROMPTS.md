# Gemini 이미지 프롬프트 — 2026-09-24 (송편)

10장 전부 아래 지시문으로 생성한다. `assets/2026-09-24/`에 이 파일명으로 넣는다.

`hook.png` `content2.png` `content3.png` `content4.png` `stat.png` `content6.png`
`content7.png` `content8.png` `content9.png` `cta.png`

계정은 `hoohihi123123`(Gemini Pro), 이미지 모드. 이 계정은 이 컴퓨터에서 `/u/2` 다.
`https://gemini.google.com/u/2/images` 로 새로 열면 새 채팅 + 이미지 모드가 한 번에 잡힌다.
**컷마다 새 채팅을 연다.** 같은 채팅에서 다음 프롬프트를 넣으면 생성이 아니라 편집으로 처리된다.

새 채팅을 연 직후 **첫 입력은 입력창에 들어가지 않는다.** 화면을 확인하고 한 번 더 타이핑한다.

다운로드는 이미지 오른쪽 위 세 아이콘 중 **맨 오른쪽**, 받은 뒤 `python grab.py 2026-09-24 <이름>`.

## 공통 블록은 셋이다

**탑다운 손만** — `hook`, `content2`, `content4`, `content6`, `content7`

```
Photorealistic documentary photograph, square 1:1 framing, shot from directly above a low table on the
floor of a Korean home. Slight film grain. Only hands and forearms enter the frame from the edges — no
faces, no heads, no shoulders, no bodies, no reflections of people. No text, no Hangul, no letters, no
numbers, no logos, no watermarks.
```

**실내-무인용** — `content3`, `stat`, `content8`, `content9`

```
Photorealistic documentary photograph, square 1:1 framing, shot indoors under warm light. Slight film
grain. No people anywhere in the frame, no hands, no faces, no bodies, no silhouettes. The subject sits in
the upper two-thirds; the bottom third is calm and uncluttered so text can sit over it. No text, no signage
lettering, no Hangul, no letters, no numbers, no logos, no watermarks.
```

**실외-무인용** — `cta`

```
Photorealistic documentary photograph, square 1:1 framing, shot outdoors in Korea at night. Slight film
grain. No people anywhere in the frame, no faces, no bodies, no silhouettes. The subject sits in the upper
two-thirds; the bottom third is calm and uncluttered so text can sit over it. No text, no signage
lettering, no Hangul, no letters, no numbers, no logos, no watermarks.
```

## 이 편에서 그림이 깨지는 지점 넷

- **송편이 만두·교자로 나온다.** 제일 크게 걸린다. 송편은 **주름이 없다.** 매끈한 반달 또는
  조개 모양, 엄지 한 마디 크기, 표면이 살짝 윤기 나는 쌀떡이다. 주름 잡힌 만두, 튀긴 교자,
  반투명 하가우, 간장 종지가 보이면 틀렸다.
- **송편이 모찌·당고로 나온다.** 동그란 공 모양, 꼬치, 가루 뿌린 떡이면 틀렸다.
- **색이 네온이 된다.** 색 송편은 **흰색, 쑥 연두, 오미자 연분홍, 치자 연노랑** 정도의 흐린 색이다.
- **솔잎이 로즈마리·전나무 가지로 나온다.** 솔잎은 가늘고 긴 바늘잎 다발이다.

---

## hook.png — 상에 늘어선 빚은 송편 (탑다운 손만 블록)

```
Directly overhead view of a low wooden floor table in a Korean home covered with rows of freshly shaped,
uncooked songpyeon — small smooth half-moon rice cakes about the size of a thumb, no pleats, no folds, in
soft white, pale mugwort green and pale pink. A large bowl of rice dough sits at one corner and small bowls
of sesame-honey filling beside it. Four pairs of hands from different edges are each pinching a rice cake
into shape, one pair clearly older and wrinkled. No dumplings with pleats, no soy sauce. Only hands and
forearms enter the frame, no faces, no heads, no shoulders. Warm light. The lower third of the frame is
bare table surface.
```

## content2.png — 송편 클로즈업 (탑다운 손만 블록)

```
Directly overhead close view of a white porcelain plate holding about a dozen steamed songpyeon — smooth
glossy half-moon Korean rice cakes with no pleats, in white, pale green and pale pink — a few strands of
pine needles stuck to their surfaces. One hand holds a single rice cake between two fingers at the edge of
the frame. Not dumplings, not mochi balls. Only hands and forearms enter the frame, no faces. Warm light.
The lower third of the frame is bare table surface.
```

## content3.png — 솔잎 깐 찜기 (실내-무인 블록)

```
Close view of a round bamboo steamer basket with its lid off, the bottom lined with a thick bed of long
thin green pine needles, rows of smooth half-moon rice cakes laid on top of the needles, soft steam rising.
It sits on a stove in a Korean home kitchen. Real pine needles — fine, long, bundled — not rosemary, not
fir branches. No people, no hands. No packaging, no labels. The lower third of the frame is plain counter.
```

## content4.png — 반쯤 베어 문 송편과 소 (탑다운 손만 블록)

```
Directly overhead view of three songpyeon rice cakes on a small white plate, each split open to show a
different filling: one with dark toasted sesame seeds and honey, one with yellow chestnut paste, one with
whole cooked beans. Beside them small bowls of each raw filling. A hand at the edge holds chopsticks. Smooth
half-moon rice cakes with no pleats. Only hands and forearms enter the frame, no faces. Warm light. The
lower third of the frame is bare table surface.
```

## stat.png — 보름달 (실내-무인 블록)

보름달이 '15'를 말한다. 창틀 너머 달, 창가 쟁반의 송편.

```
A window of a Korean apartment at night, a large bright full moon in the dark sky outside, and on the
windowsill inside a small wooden tray with a few pale half-moon rice cakes and a sprig of pine needles. Dim
warm room light. No people, no hands, no reflections of people in the glass. The lower third of the frame
is the plain dark wall below the window.
```

## content6.png — 비뚤어진 송편 하나 (탑다운 손만 블록)

예쁜 송편 옆 못생긴 송편 하나가 속담을 말한다.

```
Directly overhead view of a wooden tray of neatly shaped, perfectly smooth half-moon rice cakes in rows,
and at the front one clumsy, lopsided, cracked rice cake that is clearly badly shaped. A young hand has just
set the lopsided one down; an older wrinkled hand points at it. No pleats on any rice cake. Only hands and
forearms enter the frame, no faces. Warm light. The lower third of the frame is bare table surface.
```

## content7.png — 반죽 그릇을 둘러싼 손들 (탑다운 손만 블록)

```
Directly overhead view of a large stainless steel mixing bowl of white rice dough in the centre of a low
table on a heated wooden floor, and six or seven hands reaching in from all sides — children's small
hands, adult hands, an elderly hand — tearing off pieces of dough and rolling them into balls. Cups of tea
and a scatter of finished rice cakes around the bowl. Only hands and forearms enter the frame, no faces,
no heads. Warm light. The lower third of the frame is bare floor.
```

## content8.png — 떡집 진열대 (실내-무인 블록)

```
The display counter of a small Korean rice cake shop, stacked clear plastic trays of songpyeon in white,
pale green and pale pink, rows of other rice cakes behind them on wooden boards, a large steamer in the
back. Every tray lid, sign and price card is completely blank with no writing or numbers. No people, no
hands. The lower third of the frame is the plain counter front.
```

## content9.png — 다 찐 송편 한 접시와 차 (실내-무인 블록)

```
A single plate of steamed songpyeon with pine needles, a cup of barley tea and a small dish of sesame oil
on a low wooden table in a quiet Korean living room in the evening, a folded floor cushion beside it. No
people, no hands. The lower third of the frame is the plain wooden floor.
```

## cta.png — 보름달 아래 아파트 단지 (실외-무인 블록)

```
A Korean apartment complex at night under a large bright full moon, warm light in many windows, a small
playground and trees in the foreground, deep blue sky. No people, no figures in the windows. Every sign is
a completely blank surface. The lower third of the frame is dark empty pavement.
```
