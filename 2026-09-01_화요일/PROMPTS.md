# Gemini 이미지 프롬프트 — 2026-09-01 (자리 맡기)

10장. 파일명 그대로 `assets/2026-09-01/`에 저장할 것. 렌더러가 이 이름으로 찾는다.

`hook.png` `content2.png` `content3.png` `content4.png` `content5.png` `content6.png`
`content7.png` `stat.png` `content9.png` `cta.png`

## 공통 규칙 (모든 프롬프트 뒤에 붙임)

한 캐러셀로 읽히려면 처리 방식이 열 장 다 같아야 한다. 아래 문장을 매번 그대로 뒤에 붙인다.

```
Photorealistic documentary photograph, square 1:1 framing, contemporary Seoul.
Natural daylight, muted warm-neutral color grade, slight film grain, shallow depth of field.
Subject sits in the upper two-thirds; the bottom third is calm and uncluttered so text can sit over it.
No text, no signage, no logos, no watermarks, no recognizable faces.
```

하단 3분의 1을 비우라는 건 렌더러가 아래에서 위로 올라오는 스크림을 얹고 그 위에 글자를 앉히기 때문이다. 거기에 디테일이 몰리면 다 가려진다.

---

## 01 · `hook.png`

```
An unattended open laptop on a small cafe table in Seoul, screen glowing faintly,
a half-finished iced americano beside it, a chair pushed back and empty.
Shot from a standing eye-level angle looking down at the table. Nobody in frame.
Late afternoon light through a window. The emptiness around the laptop is the subject.
```

## 02 · `content2.png` — 자리 맡기

```
A cafe table claimed by objects and no person: a smartphone face-down, a steel tumbler,
a light jacket draped over the back of the chair. Warm wood table, minimal Korean cafe interior.
Close three-quarter angle. The arrangement should read as deliberate, like a placeholder.
```

## 03 · `content3.png` — 서울에도 카메라는 많다

```
A single white CCTV camera mounted on a grey pole against an overcast Seoul sky,
apartment towers soft and out of focus far behind it. Shot from below.
Neutral, matter-of-fact, not sinister. Plenty of empty sky in the lower part of the frame.
```

## 04 · `content4.png` — 중국은 20배

```
A dense cluster of eight or more surveillance cameras bolted to one metal pole,
all facing different directions, silhouetted against a pale hazy sky. Shot from below.
The excess is the point: too many cameras on one pole to count at a glance.
```

## 05 · `content5.png` — 카메라는 이유가 아니다

```
A laptop left alone on a cafe table in sharp focus, while blurred figures walk past
behind it in motion blur. Nobody glances at it. Shot at table height.
The passing people are anonymous shapes, no faces, no detail.
```

## 06 · `content6.png` — 떨어진 현금

```
A single folded banknote lying on the tiled floor of a subway station platform,
a hand reaching down to pick it up. Generic paper currency, no visible denomination,
no national markings. Overhead fluorescent light, worn tile, shallow focus on the note.
```

## 07 · `content7.png` — 낯선 사람에게 가방을 맡긴다

```
A backpack sitting alone on a cafe chair in the foreground, and at the next table
a person seen only from behind, shoulders and back of head, working on their own thing.
The bag is in focus, the person soft. Quiet weekday afternoon light.
```

## 08 · `stat.png` — 유실물

```
The counter of a subway lost-and-found office, shelves behind it holding rows of
recovered wallets, umbrellas and bags in numbered bins. Institutional lighting,
slightly wide angle, no staff visible. Blurred and darkened enough to sit under a large number.
```

렌더러가 stat 슬라이드에는 blur 4에 어둡게 깔기 때문에 디테일이 살짝 뭉개져도 상관없다.

## 09 · `content9.png` — 한계

```
The interior of a small unmanned Korean convenience store at night, self-checkout kiosk
glowing, a dome security camera visible on the ceiling, nobody inside.
Cold fluorescent light against the dark street outside the glass front.
Slightly uneasy, the opposite mood to the earlier slides.
```

## 10 · `cta.png` — 마무리

```
A Seoul side street at dusk, cafe windows lit warm, people walking as soft silhouettes,
shot from across the street. Wide, calm, no single subject.
Ends the set on the same city the first slide started in.
```

---

## 뽑고 나서

1. 열 장 `assets/2026-09-01/`에 파일명 그대로 저장
2. 렌더:
   ```
   python make_cards.py content/2026-09-01.json "2026-09-01_화요일/slides" ~/Desktop/koreahotshot/2026-09-01_화요일/slides
   python make_cards.py content/2026-09-01.json --ko "2026-09-01_화요일/slides_ko" ~/Desktop/koreahotshot/2026-09-01_화요일/slides_ko
   ```
3. 우하단 Gemini ✦ 마크는 렌더러가 프레임 12%를 잘라내며 같이 날린다. 지우려고 손대지 말 것

06번은 지폐 때문에 Gemini가 거부할 수 있다. 막히면 지폐 대신 떨어진 지갑으로 바꿔서 다시 뽑는다.

---

## 실제 생성 기록 (2026-08-31)

Gemini 계정 `hoohihi123123@gmail.com`, 이미지 모드(Nano Banana 2)로 10장 전부 생성. 출력은 2048x2048.

- 06번은 첫 시도에서 미국 달러 지폐가 나와서 재생성했다. "must NOT be a US dollar, no green ink, no portrait, no numerals, plain pale beige and blue-grey"를 넣으니 해결.
- 다운로드는 비동기다. 클릭 직후 바로 `~/Downloads`에서 최신 파일을 집으면 **이전 날짜 이미지를 집는다.** 실제로 06번이 08-29 등산 사진으로 덮였다가 다시 고쳤다. 파일 mtime이 방금 시각인지 확인하고 옮길 것.
