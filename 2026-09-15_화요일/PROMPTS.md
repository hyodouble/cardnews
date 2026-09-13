# Gemini 이미지 프롬프트 — 2026-09-15 (전세)

10장. 파일명 그대로 `assets/2026-09-15/`에 저장할 것. 렌더러가 이 이름으로 찾는다.

`hook.png` `content2.png` `content3.png` `content4.png` `stat.png` `content6.png`
`content7.png` `content8.png` `content9.png` `cta.png`

## 공통 규칙 (모든 프롬프트 뒤에 붙임)

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

이 편에서 그림이 깨지는 지점 넷:

- **미국 교외 주택이 나온다.** 'apartment', 'rental house'만 쓰면 잔디 마당에 목조 이층집이 나온다.
  세입자가 실제로 사는 집은 **빌라(다세대)** 아니면 **아파트 단지**다. 공통 규칙에
  `low-rise multi-family walk-ups ... red-brown brick or beige ceramic tile, external stair towers` 를 박아뒀고,
  전세사기 컷(content7)은 특히 아파트가 아니라 **빌라**여야 한다 — 피해 주택은 다세대 28.5%, 오피스텔
  20.9%, 다가구 18.7%인 반면 아파트는 13.3%다. 타워 단지를 내보내면 카드 내용과 사진이 어긋난다.

- **한글이 살아난다.** 이 편은 부동산 중개소·계약서·관공서 창구가 소재라 글자가 화면에 들어올 자리가
  많다. 중개소 유리창 전단, 계약서 본문, 창구 안내판 전부 **읽히면 안 된다.** 프롬프트마다
  `paper completely blank / illegible` 또는 `out of focus so no character is readable` 를 붙였다.
  글자가 또렷하게 나온 컷은 버리고 다시 뽑는다.

- **도장이 틀린다.** 계약에 찍는 건 서양식 고무 스탬프도 밀랍 봉인도 아니다. **인감도장**은 손가락
  두 마디 길이의 가는 원통형(나무·뿔·돌)이고, 빨간 인주가 든 납작한 원형 케이스와 함께 쓴다.
  `small cylindrical Korean name seal, wooden or horn, with a round flat tin of red seal paste` 로 고정한다.

- **돈다발이 나온다.** 보증금을 현금 뭉치로 그리면 위조지폐 문제도 있고 장면 자체가 거짓이다.
  전세금은 계좌이체로 움직인다. 지폐는 어느 컷에도 넣지 않는다.

---

## hook.png — 계약 직전의 빈 집 — 아무것도 없는 거실

```
The empty living room of a Korean flat just before a tenant moves in: bare pale laminate floor, white walls,
a wide window with the neighbourhood outside, a single set of keys lying on the floor near the middle of the
frame. Nothing else in the room. Late afternoon light falling across the floor in one long band.

Photorealistic documentary photograph, square 1:1 framing, a Korean residential neighbourhood in the late
afternoon. Korean housing, not Western housing: low-rise multi-family walk-ups four or five storeys high,
faced in red-brown brick or beige ceramic tile, external stair towers, air-conditioner units bracketed to the
walls, stainless water tanks and drying racks on the flat roofs, tangled overhead cables, a narrow street with
cars parked half on the kerb. Slab apartment towers stand behind them in the distance. Low warm sunlight,
slight film grain, shallow depth of field. Subject sits in the upper two-thirds; the bottom third is calm and
uncluttered so text can sit over it. People appear only from behind, cropped at the shoulders, or blurred.
No text, no signage lettering, no Hangul, no letters, no numbers, no logos, no watermarks, no recognizable faces.
```

## content2.png — 부동산 중개소 유리창

```
The window of a small Korean estate agency at street level, seen from the pavement outside: dozens of small
paper listings taped up in a grid behind the glass, every sheet blank or so far out of focus that no character
is readable. The dim interior shows a desk and an empty chair behind the papers. Reflections of the low-rise
brick street in the glass.

Photorealistic documentary photograph, square 1:1 framing, a Korean residential neighbourhood in the late
afternoon. Korean housing, not Western housing: low-rise multi-family walk-ups four or five storeys high,
faced in red-brown brick or beige ceramic tile, external stair towers, air-conditioner units bracketed to the
walls, stainless water tanks and drying racks on the flat roofs, tangled overhead cables, a narrow street with
cars parked half on the kerb. Slab apartment towers stand behind them in the distance. Low warm sunlight,
slight film grain, shallow depth of field. Subject sits in the upper two-thirds; the bottom third is calm and
uncluttered so text can sit over it. People appear only from behind, cropped at the shoulders, or blurred.
No text, no signage lettering, no Hangul, no letters, no numbers, no logos, no watermarks, no recognizable faces.
```

## content3.png — 계약서와 인감도장

```
Top-down view of a lease signing on a wooden desk: a stack of contract pages whose surface is completely blank
white paper, a small cylindrical Korean name seal made of dark horn standing beside it, a round flat tin of red
seal paste open next to that, and a ballpoint pen. Two pairs of hands at the edge of the frame, cropped at the
wrists. No writing, no printing, no lines on any sheet.

Photorealistic documentary photograph, square 1:1 framing, a Korean residential neighbourhood in the late
afternoon. Korean housing, not Western housing: low-rise multi-family walk-ups four or five storeys high,
faced in red-brown brick or beige ceramic tile, external stair towers, air-conditioner units bracketed to the
walls, stainless water tanks and drying racks on the flat roofs, tangled overhead cables, a narrow street with
cars parked half on the kerb. Slab apartment towers stand behind them in the distance. Low warm sunlight,
slight film grain, shallow depth of field. Subject sits in the upper two-thirds; the bottom third is calm and
uncluttered so text can sit over it. People appear only from behind, cropped at the shoulders, or blurred.
No text, no signage lettering, no Hangul, no letters, no numbers, no logos, no watermarks, no recognizable faces.
```

## content4.png — 은행 대출 창구

```
A loan desk inside a Korean bank branch, shot from behind the customer: the back of one seated person cropped
at the shoulders, a low partition, a monitor turned away from camera, a teller's hands on a keyboard with the
teller's face out of frame. Cool even ceiling light, pale interior, everything on the desk blank or blurred.

Photorealistic documentary photograph, square 1:1 framing, a Korean residential neighbourhood in the late
afternoon. Korean housing, not Western housing: low-rise multi-family walk-ups four or five storeys high,
faced in red-brown brick or beige ceramic tile, external stair towers, air-conditioner units bracketed to the
walls, stainless water tanks and drying racks on the flat roofs, tangled overhead cables, a narrow street with
cars parked half on the kerb. Slab apartment towers stand behind them in the distance. Low warm sunlight,
slight film grain, shallow depth of field. Subject sits in the upper two-thirds; the bottom third is calm and
uncluttered so text can sit over it. People appear only from behind, cropped at the shoulders, or blurred.
No text, no signage lettering, no Hangul, no letters, no numbers, no logos, no watermarks, no recognizable faces.
```

## stat.png — 원룸 빌라촌 골목, 창문마다 불

```
A dense street of Korean low-rise rental buildings at dusk, four and five storeys, brick and tiled facades
packed shoulder to shoulder, small windows lit in an irregular pattern up every floor, air-conditioner units
and rooftop water tanks against a deep blue sky. Shot down the length of the street. The empty road fills the
lower third.

Photorealistic documentary photograph, square 1:1 framing, a Korean residential neighbourhood in the late
afternoon. Korean housing, not Western housing: low-rise multi-family walk-ups four or five storeys high,
faced in red-brown brick or beige ceramic tile, external stair towers, air-conditioner units bracketed to the
walls, stainless water tanks and drying racks on the flat roofs, tangled overhead cables, a narrow street with
cars parked half on the kerb. Slab apartment towers stand behind them in the distance. Low warm sunlight,
slight film grain, shallow depth of field. Subject sits in the upper two-thirds; the bottom third is calm and
uncluttered so text can sit over it. People appear only from behind, cropped at the shoulders, or blurred.
No text, no signage lettering, no Hangul, no letters, no numbers, no logos, no watermarks, no recognizable faces.
```

## content6.png — 멈춘 아파트 공사 현장

```
A stalled apartment construction site on the edge of a Korean city: two concrete tower frames half finished,
a tower crane standing idle over them, blue safety netting on the scaffolding, a green hoarding around the
base and nobody working. Overcast flat light. The hoarding runs across the lower third, plain and unmarked.

Photorealistic documentary photograph, square 1:1 framing, a Korean residential neighbourhood in the late
afternoon. Korean housing, not Western housing: low-rise multi-family walk-ups four or five storeys high,
faced in red-brown brick or beige ceramic tile, external stair towers, air-conditioner units bracketed to the
walls, stainless water tanks and drying racks on the flat roofs, tangled overhead cables, a narrow street with
cars parked half on the kerb. Slab apartment towers stand behind them in the distance. Low warm sunlight,
slight film grain, shallow depth of field. Subject sits in the upper two-thirds; the bottom third is calm and
uncluttered so text can sit over it. People appear only from behind, cropped at the shoulders, or blurred.
No text, no signage lettering, no Hangul, no letters, no numbers, no logos, no watermarks, no recognizable faces.
```

## content7.png — 빌라 계단실, 문 앞에 쌓인 우편물

```
The interior stairwell of a Korean low-rise walk-up: a landing with two steel front doors, a bare fluorescent
tube overhead, chipped tiled steps, and a drift of unopened envelopes and paper slips piled on the floor
against one of the doors, all of them blank white with nothing printed on them. Cold light, nobody there.

Photorealistic documentary photograph, square 1:1 framing, a Korean residential neighbourhood in the late
afternoon. Korean housing, not Western housing: low-rise multi-family walk-ups four or five storeys high,
faced in red-brown brick or beige ceramic tile, external stair towers, air-conditioner units bracketed to the
walls, stainless water tanks and drying racks on the flat roofs, tangled overhead cables, a narrow street with
cars parked half on the kerb. Slab apartment towers stand behind them in the distance. Low warm sunlight,
slight film grain, shallow depth of field. Subject sits in the upper two-thirds; the bottom third is calm and
uncluttered so text can sit over it. People appear only from behind, cropped at the shoulders, or blurred.
No text, no signage lettering, no Hangul, no letters, no numbers, no logos, no watermarks, no recognizable faces.
```

## content8.png — 주민센터 민원 창구

```
A civil affairs counter inside a Korean community service centre: a long low desk, a numbered waiting area
behind it out of focus, a clerk's hands stamping a blank sheet of paper with a red ink stamp, the clerk cropped
at the shoulders. Pale institutional interior, cool ceiling light, every sign and screen blurred past reading.

Photorealistic documentary photograph, square 1:1 framing, a Korean residential neighbourhood in the late
afternoon. Korean housing, not Western housing: low-rise multi-family walk-ups four or five storeys high,
faced in red-brown brick or beige ceramic tile, external stair towers, air-conditioner units bracketed to the
walls, stainless water tanks and drying racks on the flat roofs, tangled overhead cables, a narrow street with
cars parked half on the kerb. Slab apartment towers stand behind them in the distance. Low warm sunlight,
slight film grain, shallow depth of field. Subject sits in the upper two-thirds; the bottom third is calm and
uncluttered so text can sit over it. People appear only from behind, cropped at the shoulders, or blurred.
No text, no signage lettering, no Hangul, no letters, no numbers, no logos, no watermarks, no recognizable faces.
```

## content9.png — 이사 나가는 날, 사다리차 없이 빈 방과 상자

```
A Korean flat on moving day, almost cleared: bare floor, a few taped cardboard boxes stacked by the door, pale
rectangles on the wallpaper where furniture stood, curtains gone and the window bare onto the neighbourhood.
Late afternoon light. Boxes plain brown with nothing written on them. Nobody in the room.

Photorealistic documentary photograph, square 1:1 framing, a Korean residential neighbourhood in the late
afternoon. Korean housing, not Western housing: low-rise multi-family walk-ups four or five storeys high,
faced in red-brown brick or beige ceramic tile, external stair towers, air-conditioner units bracketed to the
walls, stainless water tanks and drying racks on the flat roofs, tangled overhead cables, a narrow street with
cars parked half on the kerb. Slab apartment towers stand behind them in the distance. Low warm sunlight,
slight film grain, shallow depth of field. Subject sits in the upper two-thirds; the bottom third is calm and
uncluttered so text can sit over it. People appear only from behind, cropped at the shoulders, or blurred.
No text, no signage lettering, no Hangul, no letters, no numbers, no logos, no watermarks, no recognizable faces.
```

## cta.png — 해질녘 주택가 전경

```
A wide elevated view over a Korean residential district at sunset: a field of low-rise brick and tiled walk-ups
in the foreground with rooftop water tanks and drying racks, slab apartment towers rising behind them, windows
beginning to light up, hills and a warm orange sky along the skyline. The lower third is quiet rooftops.

Photorealistic documentary photograph, square 1:1 framing, a Korean residential neighbourhood in the late
afternoon. Korean housing, not Western housing: low-rise multi-family walk-ups four or five storeys high,
faced in red-brown brick or beige ceramic tile, external stair towers, air-conditioner units bracketed to the
walls, stainless water tanks and drying racks on the flat roofs, tangled overhead cables, a narrow street with
cars parked half on the kerb. Slab apartment towers stand behind them in the distance. Low warm sunlight,
slight film grain, shallow depth of field. Subject sits in the upper two-thirds; the bottom third is calm and
uncluttered so text can sit over it. People appear only from behind, cropped at the shoulders, or blurred.
No text, no signage lettering, no Hangul, no letters, no numbers, no logos, no watermarks, no recognizable faces.
```
