# Gemini 이미지 프롬프트 — 2026-09-03 (대리운전)

10장. 파일명 그대로 `assets/2026-09-03/`에 저장할 것. 렌더러가 이 이름으로 찾는다.

`hook.png` `content2.png` `content3.png` `content4.png` `content5.png` `content6.png`
`content7.png` `stat.png` `content9.png` `cta.png`

## 공통 규칙 (모든 프롬프트 뒤에 붙임)

```
Photorealistic documentary photograph, square 1:1 framing, contemporary South Korea.
Muted warm-neutral color grade, slight film grain, shallow depth of field.
Subject sits in the upper two-thirds; the bottom third is calm and uncluttered so text can sit over it.
No text, no signage, no logos, no brand marks, no licence plates, no watermarks, no recognizable faces.
```

이번 세트는 밤 장면이 대부분이다. 어두워도 피사체가 뭉개지지 않게 프롬프트마다
광원(가로등, 편의점 불빛, 헤드라이트)을 하나씩 명시해 뒀다. 빼지 말 것.

간판이 많이 잡히는 소재라 `no signage, no logos`가 특히 중요하다. 한글 간판이
읽히게 들어가면 다시 뽑는다.

---

## hook.png — 키를 건네는 순간

```
Night street outside a Korean restaurant. A man in a light jacket, seen from behind,
hands a car key to another man standing beside a dark sedan at the kerb. Warm light
spills from the restaurant window behind them. Both figures from behind or in profile,
faces not visible.
```

## content2.png — 뒷자리에서 본 차 안

```
Interior of a sedan at night seen over the shoulder of a passenger sitting alone in
the back seat. A driver's silhouette at the wheel ahead, the front passenger seat
empty. Streetlights and tail lights smear across the windscreen. Dashboard glow is
the only light inside.
```

## content3.png — 술자리 끝, 차 키

```
A car key lying on a restaurant table next to two empty green soju bottles and a
half-finished glass. Overhead pendant light, plates pushed aside, the table already
cleared around it. Close, shallow focus on the key.
```

## content4.png — 두고 갈 수 없는 차

```
A single parked car on an empty office-district street late at night, under one
streetlight. Shuttered storefronts, wet asphalt reflecting the light, nobody around.
Wide shot, the car small in the frame.
```

## content5.png — 트렁크 속 접이식 킥보드

```
An open car trunk at night with a folded electric kick scooter lying inside on the
carpet. The trunk lamp lights it from above; the street behind is dark. Close shot
from just behind the bumper.
```

## content6.png — 전화로 부른다

```
A man standing on a night street holding a phone to his ear, seen from behind, his
other hand in his pocket. Convenience store light washes over him from the left.
Blurred traffic passes in the background.
```

## content7.png — 아침의 주차장

```
An outdoor apartment car park at first light, one sedan parked neatly in a marked
bay, everything else empty. Cold blue morning light, long shadows, no people.
Wide, calm, symmetrical.
```

## stat.png — 밤의 인파

```
A crowded Korean restaurant alley at night, groups of people walking out and
scattering toward the main road. Warm lantern and window light, motion blur on the
walkers. Shot from above head height, faces not identifiable.
```

## content9.png — 마지막 콜이 끝난 뒤

```
A lone rider on a small electric kick scooter on an empty multi-lane road at night,
seen from behind at a distance. Headlights of a car approaching far ahead, orange
street lamps overhead. The road dominates the frame; the rider is small.
```

## cta.png — 닫는 장면

```
A quiet Seoul residential street just before dawn, cars parked along both sides,
apartment towers behind with a few windows lit. Empty road, soft blue light,
no people.
```

---

## 뽑고 나서 확인할 것

- 번호판이 읽히면 다시. 한글 간판이 읽히면 다시.
- 얼굴이 식별되면 다시. 뒷모습·실루엣이면 통과.
- 화면비와 ✦ 워터마크는 신경 쓰지 말 것. 렌더러가 우하단 12%를 잘라낸다.
