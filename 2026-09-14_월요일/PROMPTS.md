# Gemini 이미지 프롬프트 — 2026-09-14 (전세)

10장 전부 생성 완료. `assets/2026-09-14/`에 아래 파일명으로 들어 있다.

`hook.png` `content2.png` `content3.png` `content4.png` `stat.png` `content6.png`
`content7.png` `content8.png` `content9.png` `cta.png`

계정은 `hoohihi123123`(Gemini Pro), 이미지 모드(Nano Banana 2)에서 뽑았다.
**컷마다 새 채팅을 연다.** 같은 채팅에서 다음 프롬프트를 넣으면 이미지 생성이 아니라
직전 이미지의 편집으로 처리된다.

## 공통 규칙은 하나가 아니라 둘이다

처음에는 실외 묘사가 들어간 공통 규칙 하나를 열 장 전부에 붙였는데, 실내 컷이 전부 깨졌다.
`content3`(계약서 탑다운)에 실외 블록을 붙였더니 책상은 사라지고 **동네 지붕 사진**이 나왔다.
공통 블록의 "a narrow street with cars parked half on the kerb, slab apartment towers behind"가
장면 지시문을 이겨버린다. 그래서 블록을 둘로 나눴다.

**실외용** — `hook`(창밖), `content2`, `stat`, `content6`, `cta`

```
Photorealistic documentary photograph, square 1:1 framing, a Korean residential neighbourhood in the late
afternoon. Korean housing, not Western housing: low-rise multi-family walk-ups four or five storeys high,
faced in red-brown brick or beige ceramic tile, external stair towers, air-conditioner units bracketed to the
walls, stainless water tanks and drying racks on the flat roofs, tangled overhead cables, a narrow street with
cars parked half on the kerb. Slab apartment towers stand behind them in the distance. Low warm sunlight,
slight film grain, shallow depth of field. Subject sits in the upper two-thirds; the bottom third is calm and
uncluttered so text can sit over it. People appear only from behind, cropped at the shoulders, or blurred.
No text, no signage lettering, no Hangul, no letters, no numbers, no logos, no watermarks, no recognizable faces.
```

**실내용** — `content3`, `content4`, `content7`, `content8`, `content9`

```
Photorealistic documentary photograph, square 1:1 framing, shot indoors in Korea in the late afternoon.
Slight film grain, shallow depth of field. The subject sits in the upper two-thirds of the frame; the bottom
third is calm and uncluttered so text can sit over it. People appear only from behind, cropped at the
shoulders, or blurred. No text, no signage lettering, no Hangul, no letters, no numbers, no logos,
no watermarks, no recognizable faces.
```

실내 블록은 동네 묘사를 통째로 뺀 것이다. 창밖 풍경이 필요한 컷(`content9`)은 장면 지시문 안에서
`a window onto a neighbourhood of low-rise brick walk-ups with rooftop water tanks` 처럼 직접 쓴다.

## 다운로드는 1024로 줄여서 저장한다

Gemini의 '원본 크기 다운로드'는 **2048x2048**을 준다. `make_cards.py`의 워터마크 트림은
`img.size == (1024, 1024)`일 때만 동작하므로, 2048 그대로 넣으면 **✦ 워터마크가 카드에 그대로 남는다.**

```bash
sips -z 1024 1024 ~/Downloads/Gemini_Generated_Image_*.png --out assets/2026-09-14/hook.png
```

2048에서 1024로 줄이면 워터마크 위치가 비율 그대로 따라 내려가므로 12% 트림이 정확히 먹는다.
이 편 hook 컷으로 트림 후 우하단을 확대해 확인했고, 스파클은 남지 않았다.

## 이 편에서 그림이 깨지는 지점 넷

- **미국 교외 주택이 나온다.** 'apartment', 'rental house'만 쓰면 잔디 마당에 목조 이층집이 나온다.
  세입자가 실제로 사는 집은 **빌라(다세대)** 아니면 **아파트 단지**다. 실외 블록의
  `low-rise multi-family walk-ups ... red-brown brick or beige ceramic tile, external stair towers` 가 그 방어다.
  전세사기 컷(`content7`)은 특히 아파트가 아니라 **빌라**여야 한다 — 피해 주택은 다세대 28.5%,
  오피스텔 20.9%, 다가구 18.7%인 반면 아파트는 13.3%다. 타워 단지를 내보내면 카드와 사진이 어긋난다.

- **한글이 살아난다.** 이 편은 부동산 중개소·계약서·관공서 창구가 소재라 글자가 들어올 자리가 많다.
  중개소 유리창 전단, 계약서 본문, 창구 안내판 전부 읽히면 안 된다. 프롬프트마다
  `completely blank white paper` 또는 `blurred past reading` 을 붙였다. 생성분은 전부 판독 불가로 나왔다.

- **도장이 틀린다.** 서양식 고무 스탬프도 밀랍 봉인도 아니다. **인감도장**은 손가락 두 마디 길이의
  가는 원통형(나무·뿔·돌)이고, 빨간 인주가 든 납작한 원형 케이스와 함께 쓴다.
  `a small cylindrical Korean name seal made of dark horn ... a round flat tin of red seal paste` 로 고정한다.

- **돈다발이 나온다.** 보증금을 현금 뭉치로 그리면 장면 자체가 거짓이다. 전세금은 계좌이체로 움직인다.
  지폐는 어느 컷에도 넣지 않았다.

---

아래는 실제로 넣은 장면 지시문이다. 재생성할 때는 여기에 해당 공통 블록을 이어 붙인다.

## hook.png — 계약 직전의 빈 집 (실외 블록)

```
The empty living room of a Korean flat just before a tenant moves in: bare pale laminate floor, white walls,
a wide window with the neighbourhood outside, a single set of keys lying on the floor near the middle of the
frame. Nothing else in the room. Late afternoon light falling across the floor in one long band.
```

## content2.png — 부동산 중개소 유리창 (실외 블록)

```
The window of a small Korean estate agency at street level, seen from the pavement outside: dozens of small
paper listings taped up in a grid behind the glass, every sheet blank or so far out of focus that no character
is readable. The dim interior shows a desk and an empty chair behind the papers. Reflections of the low-rise
brick street in the glass.
```

## content3.png — 계약서와 인감도장 (실내 블록)

```
Top-down overhead view of a lease signing on a wooden desk, shot straight down at the desktop: a stack of
contract pages whose surface is completely blank white paper, a small cylindrical Korean name seal made of
dark horn standing on end beside the papers, a round flat tin of red seal paste open next to it, and a
ballpoint pen. Two pairs of hands enter from the edges of the frame, cropped at the wrists. No writing,
no printing, no ruled lines on any sheet.
```

## content4.png — 은행 대출 창구 (실내 블록)

```
A loan consultation desk inside a Korean bank branch, shot from behind the customer: the back of one seated
person cropped at the shoulders, a low glass partition across the desk, a computer monitor turned away from
the camera, and a teller's hands resting on a keyboard with the teller's head out of frame. Cool even ceiling
light, pale grey and white interior, every document on the desk blank and every screen and sign blurred past
reading.
```

## stat.png — 빌라촌 골목 야경 (실외 블록)

```
A dense street of Korean low-rise rental buildings at dusk, shot straight down the length of the street: four
and five storey walk-ups faced in red-brown brick and beige ceramic tile packed shoulder to shoulder, external
stair towers, air-conditioner units bracketed to the walls, stainless water tanks and drying racks on the flat
roofs, tangled overhead cables, small windows lit in an irregular pattern up every floor, slab apartment towers
rising behind them, deep blue sky. Cars parked half on the kerb. The empty road fills the lower third.
```

## content6.png — 멈춘 아파트 공사 현장 (실외 블록)

```
A stalled apartment construction site on the edge of a Korean city: two concrete tower frames left half
finished, a tower crane standing idle above them, blue safety netting hanging over the scaffolding, a plain
green metal hoarding around the base, and nobody working anywhere on the site. Overcast flat daylight, cold
grey concrete, a few Korean low-rise brick walk-ups with rooftop water tanks visible beyond the hoarding.
The hoarding runs across the lower third of the frame, plain and unmarked.
```

## content7.png — 빌라 계단실, 문 앞에 쌓인 우편물 (실내 블록)

```
The interior stairwell of a Korean low-rise walk-up building: a small landing with two steel front doors side
by side, a bare fluorescent tube on the ceiling, chipped tiled steps going up and down, scuffed pale green wall
paint, and a drift of unopened envelopes and paper slips piled on the floor against one of the doors, every
sheet blank white with nothing printed on it. Cold flat light, nobody there, quiet and still.
```

## content8.png — 주민센터 민원 창구 (실내 블록)

```
A civil affairs counter inside a Korean community service centre: a long low wooden counter across the frame,
a clerk's hands pressing a red ink stamp onto a blank sheet of paper on the counter, the clerk's head and face
out of frame above, a waiting area with rows of chairs blurred in the background. Pale institutional interior,
cool even ceiling light, every document blank and every sign and screen blurred past reading.
```

## content9.png — 이사 나가는 날, 빈 방과 상자 (실내 블록)

```
A Korean flat on moving day, almost cleared out: bare pale laminate floor, a few taped plain brown cardboard
boxes stacked by the door, faint pale rectangles on the wallpaper where furniture used to stand, curtains taken
down and the window left bare onto a neighbourhood of low-rise brick walk-ups with rooftop water tanks and slab
apartment towers behind. Late afternoon light falling across the empty floor. Nobody in the room, nothing
written on the boxes.
```

## cta.png — 해질녘 주택가 전경 (실외 블록)

```
A wide elevated view over a Korean residential district at sunset: a field of low-rise brick and beige-tiled
walk-ups in the foreground with stainless water tanks, drying racks and air-conditioner units on their flat
roofs, tangled overhead cables, slab apartment towers rising behind them, windows beginning to light up, low
hills along the skyline and a warm orange sky. The lower third of the frame is quiet uncluttered rooftops.
```
