# Gemini 이미지 프롬프트 — 2026-09-15 (한국 나이)

아직 생성 전이다. 아래 열 장을 뽑아 `assets/2026-09-15/`에 이 파일명으로 넣는다.

`hook.png` `content2.png` `content3.png` `content4.png` `stat.png` `content6.png`
`content7.png` `content8.png` `content9.png` `cta.png`

계정은 `hoohihi123123`(Gemini Pro), 이미지 모드(Nano Banana 2).
**컷마다 새 채팅을 연다.** 같은 채팅에서 다음 프롬프트를 넣으면 생성이 아니라 직전 이미지의
편집으로 처리된다.

## 공통 규칙은 둘이다

이 편은 열 컷 중 여덟이 실내다. 실외 블록의 동네 묘사가 실내 장면 지시문을 이기는 문제는
2026-09-14 편에서 확인됐으므로(계약서 탑다운에 동네 지붕이 나왔다), 블록을 나눠 쓴다.

**실외용** — `content3`, `cta`

```
Photorealistic documentary photograph, square 1:1 framing, shot outdoors in a Korean neighbourhood.
Korean streetscape, not Western: low-rise buildings faced in brick or beige ceramic tile, air-conditioner
units bracketed to the walls, stainless water tanks on the flat roofs, tangled overhead cables, a narrow
street with cars parked half on the kerb, slab apartment towers standing behind. Slight film grain, shallow
depth of field. Subject sits in the upper two-thirds; the bottom third is calm and uncluttered so text can
sit over it. People appear only from behind, cropped at the shoulders, or blurred. No text, no signage
lettering, no Hangul, no letters, no numbers, no logos, no watermarks, no recognizable faces.
```

**실내용** — 나머지 여덟 컷

```
Photorealistic documentary photograph, square 1:1 framing, shot indoors in Korea. Slight film grain, shallow
depth of field. The subject sits in the upper two-thirds of the frame; the bottom third is calm and
uncluttered so text can sit over it. People appear only from behind, cropped at the shoulders, or blurred.
No text, no signage lettering, no Hangul, no letters, no numbers, no logos, no watermarks, no recognizable faces.
```

## 다운로드는 1024로 줄여서 저장한다

Gemini의 '원본 크기 다운로드'는 **2048x2048**을 준다. `make_cards.py`의 워터마크 트림은
`img.size == (1024, 1024)`일 때만 동작하므로, 2048 그대로 넣으면 **✦ 워터마크가 카드에 그대로 남는다.**

```bash
sips -z 1024 1024 ~/Downloads/Gemini_Generated_Image_*.png --out assets/2026-09-15/hook.png
```

## 이 편에서 그림이 깨지는 지점 다섯

- **숫자를 그리고 싶어진다.** 나이가 주제라 달력, 벽시계, 번호표, 신분증, 생일 초가 전부
  자연스러운 소재로 보인다. 그런데 공통 블록이 `no numbers`를 걸고 있고, 숫자가 살아나면
  카드 위 텍스트와 충돌한다. **그래서 달력·시계·신분증 컷은 하나도 넣지 않았다.** 나이는
  음식과 몸과 줄서기로만 그린다.

- **국이 일본 것으로 나온다.** `soup`만 쓰면 미소시루가, `rice cake`만 쓰면 모찌가 나온다.
  미역국은 `miyeokguk, a dark seaweed soup in a heavy stoneware bowl`, 떡국은
  `tteokguk, a clear broth with thin oval slices of white rice cake and strips of egg and dried seaweed`
  로 못 박는다. 밥그릇도 도자기가 아니라 **스테인리스 뚜껑 공기**여야 한국 밥상이 된다.

- **교복이 세일러복으로 나온다.** 한국 교복은 재킷에 넥타이다.
  `Korean school uniform: a dark blazer with a necktie over a white shirt, no sailor collar`
  를 반드시 붙인다. 가방도 란도셀이 아니라 백팩이다.

- **아기 얼굴이 나온다.** `stat` 컷은 신생아다. 얼굴이 프레임에 들어오면 못 쓴다.
  손과 발과 천만 남기고 `the baby's face is entirely outside the frame` 를 명시한다.

- **술병 라벨이 읽힌다.** `content7`은 편의점 주류 냉장고다. 초록 병이 줄지어 서면 Gemini가
  라벨에 글자를 만든다. `every bottle label blank or blurred past reading` 를 붙인다.

---

아래가 장면 지시문이다. 재생성할 때는 해당 공통 블록을 이어 붙인다.

## hook.png — 생일상의 미역국 (실내 블록)

```
A single birthday breakfast set on a low table, shot from a low angle across the table: one heavy dark
stoneware bowl of miyeokguk, a dark seaweed soup, steam rising off it, beside a stainless steel rice bowl with
its lid set aside, a pair of stainless chopsticks and a spoon resting on the table. No candles, no cake,
nobody at the table. Warm morning light from one side, the rest of the table bare and quiet.
```

## content2.png — 새해 아침 떡국 밥상 (실내 블록)

```
A family table on New Year's morning seen from slightly above and behind one seated person cropped at the
shoulders: four or five bowls of tteokguk, a clear broth with thin oval slices of white rice cake, strips of
yellow egg and dark dried seaweed on top, set around the table with small side dishes in shallow white plates
between them. Stainless chopsticks and spoons laid beside every bowl. Everyone else is out of frame or
blurred. Pale winter daylight from a window.
```

## content3.png — 등굣길 교복 줄 (실외 블록)

```
A group of Korean secondary school students walking away from the camera up a neighbourhood street in the
morning, all seen from behind and cropped at the shoulders: dark blazers with neckties over white shirts, no
sailor collars, plain backpacks on their shoulders, all of them the same height range and moving in the same
direction. The narrow street rises slightly ahead of them between low brick buildings. Nobody's face is visible.
```

## content4.png — 병원 접수 서류 (실내 블록)

```
A hospital reception counter in Korea shot from the patient's side: a clipboard holding a single sheet of
completely blank white paper lying on the counter, a ballpoint pen on a string beside it, and a pair of hands
cropped at the wrists resting near the clipboard. Behind the counter a staff member's torso is blurred, head
out of frame. Cool even ceiling light, pale interior, every screen and sign blurred past reading, no printing
or ruled lines on the paper.
```

## stat.png — 태어난 지 이틀 (실내 블록)

```
A newborn baby wrapped in a plain white cotton hospital blanket, lying on a hospital bassinet mattress, shot
from directly above but framed on the body only: one tiny hand curled out of the blanket and the folds of the
cloth filling the frame. The baby's face is entirely outside the frame. Soft clinical light, pale white and
grey, nothing else in the shot. No wristband, no printing on the blanket.
```

## content6.png — 관공서 대기 의자 (실내 블록)

```
A row of empty waiting chairs inside a Korean government service centre, shot straight down the row: linked
grey fabric seats bolted to a steel rail, pale institutional floor tiles, one person seated at the far end
seen from behind and cropped at the shoulders. A service counter is blurred in the far background. Cool even
ceiling light, every sign and screen blurred past reading, the floor across the lower third bare and clean.
```

## content7.png — 편의점 주류 냉장고 (실내 블록)

```
The alcohol fridge of a Korean convenience store seen from the shop floor: a tall glass-doored cooler filled
with rows of green and clear bottles and canned beer, every bottle label blank or blurred past reading, cold
white light spilling from inside the cabinet across the tiled floor. One customer stands in front of it seen
from behind, cropped at the shoulders, reaching for a door handle. The rest of the shop is dim and out of focus.
```

## content8.png — 첫 만남 술자리 (실내 블록)

```
A small table in a Korean restaurant late in the evening, shot from just above the tabletop: two small
soju glasses set across from each other, one green bottle with a completely blank label between them, a
shallow plate of side dishes at the edge of the frame. Two pairs of hands enter from opposite sides of the
frame, cropped at the wrists, neither one holding a glass yet. Warm low light, both people's bodies and faces
entirely out of frame.
```

## content9.png — 현관에 벗어 놓은 신발 (실내 블록)

```
The entrance floor of a Korean home shot straight down from standing height: five or six pairs of shoes left
on the lower tiled step just inside the door, ranging from large adult shoes to small children's shoes, lined
up roughly in order of size and all pointing the same way. Plain pale tiles, the raised wooden floor of the
hallway along the top of the frame. Nobody in the shot, warm indoor light from deeper in the flat.
```

## cta.png — 해질녘 동네 전경 (실외 블록)

```
A wide elevated view over a Korean residential district at sunset: low-rise brick and beige-tiled buildings in
the foreground with stainless water tanks and air-conditioner units on their flat roofs, tangled overhead
cables, slab apartment towers rising behind them, windows beginning to light up, low hills along the skyline
and a warm orange sky. The lower third of the frame is quiet uncluttered rooftops.
```
