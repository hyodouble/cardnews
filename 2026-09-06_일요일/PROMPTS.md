# Gemini 이미지 프롬프트 — 2026-09-06 (무인민원발급기)

10장. 파일명 그대로 `assets/2026-09-06/`에 저장할 것. 렌더러가 이 이름으로 찾는다.

`hook.png` `content2.png` `content3.png` `content4.png` `content5.png` `content6.png`
`content7.png` `stat.png` `content9.png` `cta.png`

## 공통 규칙 (모든 프롬프트 뒤에 붙임)

```
Photorealistic documentary photograph, square 1:1 framing, contemporary South Korea.
Muted cool-neutral color grade, slight film grain, shallow depth of field.
Subject sits in the upper two-thirds; the bottom third is calm and uncluttered so text can sit over it.
Every screen in frame is switched off, dark, or blown out to white. No text, no signage, no Hangul,
no letters, no numbers, no logos, no brand marks, no watermarks, no recognizable faces.
```

이 편은 **화면과 서류가 주인공이라 글자가 자꾸 끼어든다.** 공통 규칙에 화면 끄는 문장을
넣어둔 건 그래서다. 빼면 제미나이가 가짜 한글을 화면과 종이에 그려 넣고, 카드 위에 얹은
영어 문구랑 충돌한다.

신분증은 특히 조심할 것. 실제 주민등록증 레이아웃이나 숫자가 보이면 그 장은 버린다.
프롬프트마다 `blank plain card, no printing` 을 박아뒀다.

기계는 은색·짙은 회색 몸체에 파란 계열 포인트가 흔하다. 색을 안 박으면 서양 ATM이나
공항 체크인 기계처럼 나온다.

---

## hook.png — 지하철 역사 안 발급기

```
A single self-service government kiosk standing against a tiled wall in a Seoul subway
station concourse late in the evening: brushed silver and dark grey body, waist-high panel,
one adult standing at it seen from behind. Cool overhead fluorescent light, polished floor
holding a soft reflection. The kiosk screen is dark and reflective.
```

## content2.png — 카드 넣는 손

```
Close crop on two hands at a self-service kiosk panel, one hand sliding a blank plain white
plastic card with no printing into a card slot, the other resting near a small square
fingerprint reader. Brushed metal panel, cool blue-grey light from above, background thrown
far out of focus.
```

## content3.png — 마트 입구 옆에 선 기계

```
A government self-service kiosk installed against the wall just inside the entrance of a
large Korean supermarket, shoppers walking past it as a soft blur, nobody stopping. Wide
daylight-balanced interior lighting, wide shot from across the aisle. Kiosk screen dark.
```

## content4.png — 서류가 나오는 순간

```
Close on a printed sheet of plain white paper emerging from a horizontal output slot on a
metal kiosk panel, a hand reaching to take it. The paper is completely blank with no printing
at all. Cool light, very shallow depth of field, the machine body soft behind it.
```

## content5.png — 집에서 뽑는 쪽

```
A quiet home desk in the early morning: a small white inkjet printer with one blank sheet
half-fed out of it, a closed laptop beside it, a mug. Soft window light from the left, warm
neutral wood surface, no screens visible, no papers with any printing.
```

## content6.png — 지갑 속 신분증

```
An overhead close shot of an open slim wallet on a plain dark table, one blank plain card
with no printing sitting in the card slot. Soft directional light, deep shadow around the
edges, very shallow depth of field so only the card edge is sharp.
```

## content7.png — 사람이 기다리는 창구

```
An almost empty public office waiting area: rows of moulded plastic chairs facing a service
counter, two people seated far apart and turned away, an unattended counter position behind
glass. Flat institutional daylight, wide symmetrical framing. All display boards blank.
```

숫자 슬라이드 바로 앞이라 여기서 온도를 한 번 떨어뜨린다. 기계 쪽 컷은 다 정돈돼 있고
이 장만 비어 있고 지루해야 7번 문구("다른 나라는 창구에 하루를 쓴다")가 산다.

## stat.png — 발급기 여러 대 (배경용)

```
A row of three identical self-service government kiosks side by side in a bright public
building lobby, seen from a distance at a slight angle, no people. Large calm wall and floor
area around them. Even diffuse lighting, all screens dark.
```

숫자가 크게 얹히고 배경은 흐려지고 어두워진다. 디테일보다 **여백**이 중요한 장이다.

## content9.png — 외국인 서류가 놓인 창구

```
A public office counter seen from the visitor's side: a plain blank white card and a plain
dark navy passport-style booklet with no emblem and no lettering lying on the counter next to
a blank printed form and a pen. A staff member's hands rest out of focus behind the counter
glass. Even daylight-balanced interior light, shallow depth of field.
```

여권·등록증이 소품인데 **실물 문양이 들어가면 그 장은 버린다.** 국장·국명·번호가 보이면
특정 국가 여권이 되고, 카드가 하려는 말("등록된 외국인은 같은 창구를 쓴다")이 아니라
어느 나라 사람 얘기가 된다. `no emblem, no lettering` 을 프롬프트에서 빼지 말 것.

앞선 그늘 버전(꺼진 기계 + 안내문)은 폐기했다. 9번이 더 이상 사고 얘기가 아니다.

## cta.png — 동네 행정복지센터 앞

```
The exterior of a small neighbourhood public service building on a quiet Sunday morning:
low modern facade, glass doors, a few potted plants, an empty bicycle rack, low autumn sun
across the pavement. No people, no signage of any kind, no lettering on the glass.
```
