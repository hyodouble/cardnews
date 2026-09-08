# Gemini 이미지 프롬프트 — 2026-09-09 (지하철 노약자석)

10장. 파일명 그대로 `assets/2026-09-09/`에 저장할 것. 렌더러가 이 이름으로 찾는다.

`hook.png` `content2.png` `content3.png` `content4.png` `content5.png` `content6.png`
`stat.png` `content8.png` `content9.png` `cta.png`

## 공통 규칙 (모든 프롬프트 뒤에 붙임)

```
Photorealistic documentary photograph, square 1:1 framing, contemporary Seoul subway interior.
Cool fluorescent light, stainless steel and pale grey panels, slight film grain, shallow depth
of field. Subject sits in the upper two-thirds; the bottom third is calm and uncluttered so
text can sit over it. Long upholstered bench seats running along the carriage wall, never
individual bucket seats. No text, no signage, no Hangul, no letters, no numbers, no route maps,
no advertising panels, no logos, no watermarks, no recognizable faces — passengers seen from
behind, cropped at the shoulders, or blurred.
```

이 편은 **지하철 내부라 글자가 반드시 낀다.** 노선도, 광고판, 출입문 위 전광판, 좌석 위
안내 스티커가 전부 글자다. 공통 규칙의 `no route maps, no advertising panels` 를 빼면
읽히지 않는 가짜 한글이 화면 절반을 채운다. 그래도 글자가 보이면 그 장은 버린다.

세 가지를 더 조심할 것:

- **서양식 지하철이 된다.** 형태를 안 박으면 뉴욕·런던식 개별 좌석과 좁은 통로가 나온다.
  한국 전동차는 **벽을 따라 길게 붙은 벤치 좌석**과 넓고 평평한 바닥이다. 프롬프트마다
  `long upholstered bench seat running along the carriage wall` 를 박아뒀다.
- **비어 있는 게 안 보인다.** 이 편의 전부는 '만원인데 저기만 비었다'이므로 프롬프트에
  빈 좌석과 서 있는 승객을 **같은 화면**에 넣어야 한다. `packed with standing passengers`
  와 `the end bench completely empty` 를 한 문장에 함께 쓴다.
- **노약자석 색이 안 산다.** 구분이 없으면 그냥 빈 자리로 읽힌다. 노약자석은 나머지
  좌석과 **다른 색 천**이고 임산부석은 **분홍**이다. 색을 직접 지정했다.

---

## hook.png — 만원 전동차, 끝 벤치만 비어 있음

```
Interior of a crowded Seoul subway car at rush hour, standing passengers packed shoulder to
shoulder down the aisle holding overhead straps, seen from mid-carriage, while the short bench
seat at the very end of the car sits completely empty — its upholstery a different colour from
the rest of the seats. Bright even ceiling light, stainless poles, the empty bench small and
obvious in the middle distance.
```

## content2.png — 노약자석 벤치 클로즈업

```
A short upholstered bench seat at the end of a Seoul subway car, six places wide, upholstered
in a distinctly different colour from the long bench beside it, completely empty, a stainless
steel partition and vertical pole at its edge. Slight angle, clean fluorescent light, no one
in frame.
```

## content3.png — 1980년의 흔적 / 규칙이 아니라 관습

```
An empty end bench in a Seoul subway car photographed straight on from the opposite seat, worn
upholstery, a stainless partition on each side, the carriage beyond it out of focus with a few
standing legs visible. Plain, documentary, nothing marked or posted anywhere in frame.
```

## content4.png — 앉으면 계산이 시작된다

```
Over-the-shoulder view from a seated passenger's position inside a Seoul subway car, hands
resting on a bag in the lower frame, looking across the aisle at the doors where standing
passengers wait, everyone cropped at the shoulders or turned away. Slight motion blur in the
standing crowd, sharp on the near hands.
```

## content5.png — 아무도 안 와도 비어 있음

```
A nearly empty Seoul subway car in daylight, one or two seated passengers far down the long
bench seen from behind, and the differently coloured end bench closest to camera left entirely
empty. Wide flat floor, low sun through the window, quiet off-peak feeling.
```

## content6.png — 분홍 임산부석은 채워진다

```
A single pink upholstered seat at the end of a row of grey-blue bench seats inside a Seoul
subway car, a passenger sitting in it cropped at the shoulders so the face is out of frame,
the seats on either side occupied too. Even ceiling light, the pink seat clearly the odd colour
in the row.
```

## stat.png — 분홍 좌석 열, 절반은 사람

```
A row of pink-upholstered priority seats along the wall of a Seoul subway car, several taken by
seated passengers cropped below the neck, one or two places empty between them, shot straight
on from across the aisle. Flat frontal composition, pink upholstery dominant, faces never in
frame.
```

## content8.png — 계산서 / 고령 승객과 개찰구

```
An older passenger seen from behind passing through a subway fare gate in Seoul, walking away
from camera into a wide bright concourse, stainless gates in a row, other commuters blurred in
motion around them. Cool overhead light, deep empty concourse beyond, nothing written anywhere
in frame.
```

## content9.png — 초고령사회 / 비어 있는 좌석의 정체

```
A Seoul subway car interior at the end of the day, the differently coloured end bench empty in
the foreground, one elderly passenger seated far down the carriage seen from behind, the rest
of the seats occupied. Long view down the length of the car, cool light, quiet.
```

## cta.png — 전동차를 빠져나가는 사람들

```
Passengers stepping off a train onto a Seoul subway platform seen from inside the car, doors
open, backs to camera, the emptied carriage interior in the foreground with its end bench still
vacant. Platform light spilling in, motion in the departing crowd, no faces.
```
