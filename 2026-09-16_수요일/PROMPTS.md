# Gemini 이미지 프롬프트 — 2026-09-16 (MBTI)

10장 전부 아래 지시문으로 생성한다. `assets/2026-09-16/`에 이 파일명으로 넣는다.

`hook.png` `content2.png` `content3.png` `content4.png` `stat.png` `content6.png`
`content7.png` `content8.png` `content9.png` `cta.png`

계정은 `hoohihi123123`(Gemini Pro), 이미지 모드(Nano Banana 2).
**컷마다 새 채팅을 연다.** 같은 채팅에서 다음 프롬프트를 넣으면 생성이 아니라 직전 이미지의
편집으로 처리된다.

## 공통 규칙은 둘이다

이 편은 열 컷 중 여덟이 실내다. 실외 블록의 동네 묘사가 실내 장면 지시문을 이기는 문제는
2026-09-14 편에서 확인됐으므로(계약서 탑다운에 동네 지붕이 나왔다), 블록을 나눠 쓴다.

**실외용** — `content9`, `cta`

```
Photorealistic documentary photograph, square 1:1 framing, shot outdoors in a Korean neighbourhood.
Korean streetscape, not Western: low-rise buildings faced in brick or beige ceramic tile, air-conditioner
units bracketed to the walls, stainless water tanks on the flat roofs, tangled overhead cables, a narrow
street with cars parked half on the kerb, slab apartment towers standing behind. Slight film grain, shallow
depth of field. Subject sits in the upper two-thirds; the bottom third is calm and uncluttered so text can
sit over it. People appear only from behind, cropped at the shoulders, or blurred. No text, no signage
lettering, no Hangul, no letters, no numbers, no logos, no watermarks, no recognizable faces.
```

**실내용** — `hook`, `content3`, `content4`, `content6`, `content7`

```
Photorealistic documentary photograph, square 1:1 framing, shot indoors in Korea. Slight film grain, shallow
depth of field. The subject sits in the upper two-thirds of the frame; the bottom third is calm and
uncluttered so text can sit over it. People appear only from behind, cropped at the shoulders, or blurred.
No text, no signage lettering, no Hangul, no letters, no numbers, no logos, no watermarks, no recognizable faces.
```

**무인용** — `content2`, `stat`, `content8`. 실내 블록의 `People appear only from behind` 는
**사람을 넣으라는 지시로 읽힌다.** 무인 탑다운 컷에 실내 블록을 쓰면 배경에 손님이 깔린다
(아래 함정 참고). 그래서 이 세 컷은 블록 자체를 바꾼다.

```
Photorealistic documentary photograph, square 1:1 framing, shot indoors in Korea. Slight film grain. No people
anywhere in the frame, no hands, no faces, no bodies, no chairs, no room, no background, no window. No text,
no signage lettering, no Hangul, no letters, no numbers, no logos, no watermarks.
```

## 다운로드는 1024로 줄여서 저장한다

Gemini의 '원본 크기 다운로드'는 **2048x2048**을 준다. `make_cards.py`의 워터마크 트림은
`img.size == (1024, 1024)`일 때만 동작하므로, 2048 그대로 넣으면 **✦ 워터마크가 카드에 그대로 남는다.**

Windows:

```bash
python -c "from PIL import Image; Image.open(r'C:/Users/기획운영실/Downloads/Gemini_Generated_Image_xxxx.png').convert('RGB').resize((1024,1024), Image.LANCZOS).save('assets/2026-09-16/hook.png')"
```

Mac(이 컴퓨터):

```bash
sips -z 1024 1024 ~/Downloads/Gemini_Generated_Image_xxxx.png --out assets/2026-09-16/hook.png
```

다운로드가 파일로 떨어지기까지 클릭 후 8~15초가 걸린다. 그 전에 `~/Downloads` 를
훑으면 **직전 편의 남은 파일을 집어간다** — 실제로 한 번 그렇게 엉뚱한 사진이
`content2.png` 로 저장됐다. 최근 3분 안에 생성된 파일만 고르도록 막아 두고 쓸 것.

## 이 편에서 그림이 깨지는 지점 일곱

- **실내 공통블록이 무인 컷을 이긴다.** 실제로 `content2`를 실내 블록으로 돌렸더니 탑다운이
  눈높이로 바뀌고 배경에 카페 손님이 가득 찼다. 블록의 `People appear only from behind,
  cropped at the shoulders, or blurred` 를 모델이 **사람을 넣으라는 지시로 읽는다.** 무인 컷은
  위의 무인 블록을 쓰고, 장면 지시문 첫 문장을 카메라 위치(`camera mounted directly above ...
  at 90 degrees`)로 시작해 `no room, no background, no window` 까지 박아야 한 번에 나온다.
  `content8`처럼 손 하나만 필요한 컷은 무인 블록을 쓰되 첫 줄에 `Correction: one single hand IS
  allowed` 로 예외를 명시한다.

- **주제가 글자라서 모델이 글자를 그리고 싶어한다.** 이 편의 소재는 네 글자다. 공고문, 폰 화면,
  명함, 이름표가 장면마다 나오는데 전부 글자가 들어갈 자리다. 공통 블록의 `no letters` 하나로는
  진다 — **종이·화면·명함이 나오는 컷은 컷마다 따로 '백지' 또는 '읽을 수 없게 블러'를 다시
  박아 둔다.** 아래 지시문에 이미 들어가 있으니 재생성할 때 지우지 말 것.

- **아이스 아메리카노가 서양 커피로 나온다.** `iced coffee`만 쓰면 유리잔에 담긴 라떼가 나온다.
  한국 카페 잔은 **뚜껑이 돔형인 투명 플라스틱 테이크아웃 컵에 얼음이 가득**이다.
  `a tall clear plastic cup with a domed lid and a straw, filled to the top with ice` 로 못 박는다.

- **취업 정장이 서양 오피스룩으로 나온다.** 한국 면접 정장은 검정이나 짙은 남색 수트에 흰 셔츠,
  장식 없음이다. `plain matching dark navy or black suit over a white shirt, no patterns, no bright colours`
  를 붙인다. 캐주얼 재킷이나 밝은 색이 나오면 면접장으로 안 읽힌다.

- **명함이 서양식으로 나온다.** `content6`은 명함 주고받는 손이다. 로고와 글자가 반드시 생기므로
  `the card is completely blank white card stock, no printing of any kind` 를 붙이고,
  **양손으로 주고받는 자세**(`both hands, held with two hands at the edges`)를 명시한다.
  한 손으로 건네면 한국 장면이 아니다.

- **사람을 넣으면 얼굴이 따라온다.** 면접 대기실(`content4`)과 인사 장면(`content9`)이 위험하다.
  두 컷 다 **뒤에서 찍거나 어깨에서 자른다**를 장면 지시문에 다시 쓴다. 그래도 얼굴이 들어오면
  재생성보다 **탑다운이나 손만 나오는 구도로 바꾸는 편이 싸다**(2026-09-15 편에서 확인).

- **카페가 미국식으로 나온다.** 한국 카페는 밝은 원목이나 노출 콘크리트, 큰 창, 낮은 테이블이다.
  `Korean cafe interior: pale wood and exposed concrete, large windows, low tables` 를 붙인다.
  벽돌벽에 칠판 메뉴판이 나오면 미국 카페다.

---

아래가 장면 지시문이다. 재생성할 때는 해당 공통 블록을 이어 붙인다.

## hook.png — 카페 유리문에 붙은 구인 공고 (실내 블록)

카드 문구가 "INFP·INTP·INTJ 지원 불가"라고 적힌 공고를 인용한다. 공고문을 그리되
**글자는 한 자도 없어야** 하므로 백지 한 장을 붙인 것으로 간다. 맥락이 글자를 대신한다.

```
Shot from inside a small Korean cafe looking out through its glass door: a single sheet of completely blank
white A4 paper taped at four corners to the inside of the glass at eye height, slightly curled at one edge.
Korean cafe interior in the foreground, pale wood and exposed concrete, out of focus. Through the glass
behind the paper, a narrow street is visible but blurred past reading. The paper carries no printing, no
ruled lines, no handwriting, nothing at all. Cool daylight, the lower third of the frame is bare floor.
```

## content2.png — 카페 테이블 위 엎어 둔 폰 두 대 (실내 블록, 탑다운)

"모두가 자기 네 글자를 안다"를 사람 없이 그린다. 얼굴이 들어올 자리를 아예 없애려고
탑다운으로 잡는다.

```
Top-down overhead flat-lay: the camera is mounted directly above the table pointing straight down at 90
degrees, and the pale wood tabletop fills the entire frame edge to edge so nothing else is visible. Lying on the
tabletop: two smartphones face down side by side, two tall clear plastic cups with domed lids and straws filled
to the top with ice and dark iced americano with condensation running down them, and one folded paper napkin
between them. Soft even daylight from one side. The lower third of the tabletop is bare and uncluttered. No
printing on the napkin, no logos on the cups, no lettering anywhere.
```

## content3.png — 소개팅 앱을 보는 손 (실내 블록)

```
A single pair of hands cropped at the wrists holding a smartphone upright above a cafe table, shot from just
behind and above the phone so the screen is visible but completely blurred past reading, a soft glow with no
discernible shapes or text. A tall clear plastic cup with a domed lid and a straw, full of ice, stands on the
pale wood table below. Korean cafe interior behind, large window light, everything past the hands out of
focus. No face, no head, no body in the frame. The screen shows no readable content of any kind.
```

## content4.png — 면접 대기실 (실내 블록)

```
A row of young jobseekers seated along a wall of linked grey chairs in a Korean office waiting area, all seen
from directly behind and cropped at the shoulders so no face or head is visible: each in a plain matching
dark navy or black suit over a white shirt, no patterns and no bright colours, each holding a plain document
folder flat on their knees. Pale institutional wall and floor tiles, a blurred reception counter far down the
corridor. Cool even ceiling light, every sign and screen blurred past reading, the floor across the lower
third bare. No printing on the folders.
```

## stat.png — 책상에 펼쳐 놓은 서류 봉투 더미 (실내 블록, 탑다운)

3.1%는 "752곳 중 23곳"이다. 많은 것 가운데 몇 개를 그리되, 숫자를 세게 만들면 안 되므로
봉투는 균일하게 깔고 개수를 강조하지 않는다.

```
Top-down overhead flat-lay: the camera is mounted directly above a desk pointing straight down at 90 degrees,
and the desk surface fills the entire frame edge to edge so nothing else is visible. Covering the desk edge to
edge, plain manila document envelopes laid out in overlapping rows, all the same size and all completely blank
with no printing, labels, stamps or handwriting of any kind. A few sit slightly askew from the rest. Cool even
light from above. The lower third has fewer envelopes and more bare dark desk surface.
```

## content6.png — 양손으로 주고받는 명함 (실내 블록)

```
Two pairs of hands meeting over a table in a Korean office, cropped at the wrists, exchanging a business
card: the giver holds the card at its two bottom corners with both hands and offers it forward, the receiver
reaches with both hands to take it at the top corners. The card is completely blank white card stock with no
printing of any kind, no logo, no lines. Dark suit cuffs and white shirt cuffs at the edges of the frame.
Both people's bodies and faces are entirely out of frame. Warm indoor light, a blurred office interior
behind, the lower third of the table bare.
```

## content7.png — 식어 버린 커피와 마주 놓인 두 손 (실내 블록)

"너 T야?"가 나오는 순간, 대화가 식은 자리다.

```
A cafe table shot from just above the tabletop: one tall clear plastic cup of iced americano half finished,
the ice melted down to slivers and a ring of condensation pooled around the base, and a second cup pushed
further away and untouched. Two hands rest on the table from opposite sides, cropped at the wrists, not
touching each other and not holding either cup. Pale wood table, Korean cafe interior blurred behind, large
window light going flat and grey. Both people's bodies and faces entirely out of frame. No logos on the cups.
```

## content8.png — 백지 서류 위에 멈춘 펜 (실내 블록)

"다른 나라에선 사적인 정보"를 망설임으로 그린다.

```
Correction: one single hand IS allowed in this shot and nothing else of the person. Top-down overhead close
view, camera pointing straight down at a desk: one hand cropped cleanly at the wrist holds a ballpoint pen
stopped just above a sheet of completely blank white paper, the pen tip not touching the page, held still. The
paper has no printing, no ruled lines, no boxes and no handwriting. A plain closed document folder lies beside
it. Plain pale desk surface fills the frame, cool even light from above, the lower third of the desk bare. No
arm beyond the wrist, no body, no face, nothing else in the frame.
```

## content9.png — 골목에서 나누는 첫 인사 (실외 블록)

```
Two people meeting on a narrow Korean neighbourhood street, both seen from behind and to one side and cropped
at the shoulders so neither face is visible, each bowing slightly toward the other from the waist with arms
held straight down, a small gap of pavement between them. One carries a plain shoulder bag. Low brick and
beige-tiled buildings with air-conditioner units on the walls line the street behind them, cars parked half
on the kerb. Late afternoon light from one side, the lower third of the frame is bare pavement.
```

## cta.png — 해질녘 동네 전경 (실외 블록)

```
A wide elevated view across a Korean residential district at dusk, looking down a long shallow valley of
rooftops: low-rise brick and beige-tiled buildings with stainless water tanks and air-conditioner units on
their flat roofs, tangled overhead cables strung between poles, slab apartment towers rising along both
sides with their windows lighting up one by one, low dark hills closing the skyline and a deep orange sky
above them. The lower third of the frame is quiet uncluttered rooftops in shadow.
```
