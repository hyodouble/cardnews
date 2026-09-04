# 붙여넣기용 — 2026-09-06 (무인민원발급기) 10장

각 블록 통째로 복사해서 Gemini 이미지 모드에 붙여넣기. 공통 규칙 이미 포함됨.
저장 위치: `~/projects/cardnews/assets/2026-09-06/<파일명>`

이 편만의 함정 두 개:

- **화면과 종이에 가짜 한글이 그려진다.** 공통 규칙에 화면 끄고 종이 비우는 문장이 들어가 있다. 그래도 글자가 나오면 그 장은 버리고 다시 뽑는다.
- **신분증·여권에 실물 문양이 들어가면 버린다.** 6번과 9번이 특히 그렇다. 국장이나 번호가 보이면 특정 국가 얘기가 되어버린다.

화면비나 제미나이 워터마크 때문에는 절대 다시 뽑지 않는다 — `make_cards.py`가 12% 잘라낸다. README의 *Generating the photos* 참고.

---
## 1. hook.png — 지하철 역사 안 발급기
```
A single self-service government kiosk standing against a tiled wall in a Seoul subway station concourse late in the evening: brushed silver and dark grey body, waist-high panel, one adult standing at it seen from behind. Cool overhead fluorescent light, polished floor holding a soft reflection. The kiosk screen is dark and reflective.

Photorealistic documentary photograph, square 1:1 framing, contemporary South Korea. Muted cool-neutral color grade, slight film grain, shallow depth of field. Subject sits in the upper two-thirds; the bottom third is calm and uncluttered so text can sit over it. Every screen in frame is switched off, dark, or blown out to white. No text, no signage, no Hangul, no letters, no numbers, no logos, no brand marks, no watermarks, no recognizable faces.
```

---
## 2. content2.png — 카드 넣는 손
```
Close crop on two hands at a self-service kiosk panel, one hand sliding a blank plain white plastic card with no printing into a card slot, the other resting near a small square fingerprint reader. Brushed metal panel, cool blue-grey light from above, background thrown far out of focus.

Photorealistic documentary photograph, square 1:1 framing, contemporary South Korea. Muted cool-neutral color grade, slight film grain, shallow depth of field. Subject sits in the upper two-thirds; the bottom third is calm and uncluttered so text can sit over it. Every screen in frame is switched off, dark, or blown out to white. No text, no signage, no Hangul, no letters, no numbers, no logos, no brand marks, no watermarks, no recognizable faces.
```

---
## 3. content3.png — 마트 입구 옆에 선 기계
```
A government self-service kiosk installed against the wall just inside the entrance of a large Korean supermarket, shoppers walking past it as a soft blur, nobody stopping. Wide daylight-balanced interior lighting, wide shot from across the aisle. Kiosk screen dark.

Photorealistic documentary photograph, square 1:1 framing, contemporary South Korea. Muted cool-neutral color grade, slight film grain, shallow depth of field. Subject sits in the upper two-thirds; the bottom third is calm and uncluttered so text can sit over it. Every screen in frame is switched off, dark, or blown out to white. No text, no signage, no Hangul, no letters, no numbers, no logos, no brand marks, no watermarks, no recognizable faces.
```

---
## 4. content4.png — 서류가 나오는 순간
```
Close on a printed sheet of plain white paper emerging from a horizontal output slot on a metal kiosk panel, a hand reaching to take it. The paper is completely blank with no printing at all. Cool light, very shallow depth of field, the machine body soft behind it.

Photorealistic documentary photograph, square 1:1 framing, contemporary South Korea. Muted cool-neutral color grade, slight film grain, shallow depth of field. Subject sits in the upper two-thirds; the bottom third is calm and uncluttered so text can sit over it. Every screen in frame is switched off, dark, or blown out to white. No text, no signage, no Hangul, no letters, no numbers, no logos, no brand marks, no watermarks, no recognizable faces.
```

---
## 5. content5.png — 집에서 뽑는 쪽
```
A quiet home desk in the early morning: a small white inkjet printer with one blank sheet half-fed out of it, a closed laptop beside it, a mug. Soft window light from the left, warm neutral wood surface, no screens visible, no papers with any printing.

Photorealistic documentary photograph, square 1:1 framing, contemporary South Korea. Muted cool-neutral color grade, slight film grain, shallow depth of field. Subject sits in the upper two-thirds; the bottom third is calm and uncluttered so text can sit over it. Every screen in frame is switched off, dark, or blown out to white. No text, no signage, no Hangul, no letters, no numbers, no logos, no brand marks, no watermarks, no recognizable faces.
```

---
## 6. content6.png — 지갑 속 신분증
```
An overhead close shot of an open slim wallet on a plain dark table, one blank plain card with no printing sitting in the card slot. Soft directional light, deep shadow around the edges, very shallow depth of field so only the card edge is sharp.

Photorealistic documentary photograph, square 1:1 framing, contemporary South Korea. Muted cool-neutral color grade, slight film grain, shallow depth of field. Subject sits in the upper two-thirds; the bottom third is calm and uncluttered so text can sit over it. Every screen in frame is switched off, dark, or blown out to white. No text, no signage, no Hangul, no letters, no numbers, no logos, no brand marks, no watermarks, no recognizable faces.
```

---
## 7. content7.png — 사람이 기다리는 창구
```
An almost empty public office waiting area: rows of moulded plastic chairs facing a service counter, two people seated far apart and turned away, an unattended counter position behind glass. Flat institutional daylight, wide symmetrical framing. All display boards blank.

Photorealistic documentary photograph, square 1:1 framing, contemporary South Korea. Muted cool-neutral color grade, slight film grain, shallow depth of field. Subject sits in the upper two-thirds; the bottom third is calm and uncluttered so text can sit over it. Every screen in frame is switched off, dark, or blown out to white. No text, no signage, no Hangul, no letters, no numbers, no logos, no brand marks, no watermarks, no recognizable faces.
```

---
## 8. stat.png — 발급기 여러 대 (배경용)
```
A row of three identical self-service government kiosks side by side in a bright public building lobby, seen from a distance at a slight angle, no people. Large calm wall and floor area around them. Even diffuse lighting, all screens dark.

Photorealistic documentary photograph, square 1:1 framing, contemporary South Korea. Muted cool-neutral color grade, slight film grain, shallow depth of field. Subject sits in the upper two-thirds; the bottom third is calm and uncluttered so text can sit over it. Every screen in frame is switched off, dark, or blown out to white. No text, no signage, no Hangul, no letters, no numbers, no logos, no brand marks, no watermarks, no recognizable faces.
```

---
## 9. content9.png — 외국인 서류가 놓인 창구
```
A public office counter seen from the visitor's side: a plain blank white card and a plain dark navy passport-style booklet with no emblem and no lettering lying on the counter next to a blank printed form and a pen. A staff member's hands rest out of focus behind the counter glass. Even daylight-balanced interior light, shallow depth of field.

Photorealistic documentary photograph, square 1:1 framing, contemporary South Korea. Muted cool-neutral color grade, slight film grain, shallow depth of field. Subject sits in the upper two-thirds; the bottom third is calm and uncluttered so text can sit over it. Every screen in frame is switched off, dark, or blown out to white. No text, no signage, no Hangul, no letters, no numbers, no logos, no brand marks, no watermarks, no recognizable faces.
```

---
## 10. cta.png — 동네 행정복지센터 앞
```
The exterior of a small neighbourhood public service building on a quiet Sunday morning: low modern facade, glass doors, a few potted plants, an empty bicycle rack, low autumn sun across the pavement. No people, no signage of any kind, no lettering on the glass.

Photorealistic documentary photograph, square 1:1 framing, contemporary South Korea. Muted cool-neutral color grade, slight film grain, shallow depth of field. Subject sits in the upper two-thirds; the bottom third is calm and uncluttered so text can sit over it. Every screen in frame is switched off, dark, or blown out to white. No text, no signage, no Hangul, no letters, no numbers, no logos, no brand marks, no watermarks, no recognizable faces.
```
