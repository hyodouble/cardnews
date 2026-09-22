# Gemini 이미지 프롬프트 — 2026-09-22 (산후조리원)

10장 전부 아래 지시문으로 생성한다. `assets/2026-09-22/`에 이 파일명으로 넣는다.

`hook.png` `content2.png` `content3.png` `content4.png` `stat.png` `content6.png`
`content7.png` `content8.png` `content9.png` `cta.png`

계정은 `hoohihi123123`(Gemini Pro), 이미지 모드(Nano Banana 2).
**컷마다 새 채팅을 연다.** 같은 채팅에서 다음 프롬프트를 넣으면 생성이 아니라 직전 이미지의
편집으로 처리된다. `https://gemini.google.com/u/1/images` 로 새로 열면 새 채팅 + 이미지 모드가
한 번에 잡힌다.

## 공통 블록은 넷이다

블록의 `People appear only from behind` 는 모델이 **사람을 넣으라는 지시로 읽는다.** 무인 컷에
인물 블록을 쓰면 배경에 사람이 깔리므로 컷 성격대로 나눠 쓴다. 이 편은 무인 컷이 넷이다.

**시설-인물용** — `hook`, `content6`, `content8`

```
Photorealistic documentary photograph, square 1:1 framing, shot indoors in a modern Korean postpartum care
centre under soft warm light. Slight film grain, shallow depth of field. The subject sits in the upper
two-thirds of the frame; the bottom third is calm and uncluttered so text can sit over it. People appear
only from behind, cropped at the shoulders, or blurred. No text, no signage lettering, no Hangul, no
letters, no numbers, no logos, no watermarks, no recognizable faces.
```

**탑다운 손만** — `content3`, `stat`, `content9`

```
Photorealistic documentary photograph, square 1:1 framing, shot from directly above a table in a Korean
interior. Slight film grain. Only hands and forearms enter the frame from the edges — no faces, no heads,
no shoulders, no bodies, no reflections of people. No text, no signage lettering, no Hangul, no letters, no
numbers, no logos, no watermarks.
```

**실내-무인용** — `content2`, `content4`, `content7`

```
Photorealistic documentary photograph, square 1:1 framing, shot indoors under soft warm light. Slight film
grain. No people anywhere in the frame, no hands, no faces, no bodies, no silhouettes. The subject sits in
the upper two-thirds; the bottom third is calm and uncluttered so text can sit over it. No text, no signage
lettering, no Hangul, no letters, no numbers, no logos, no watermarks.
```

**실외-무인용** — `cta`

```
Photorealistic documentary photograph, square 1:1 framing, shot outdoors on a Korean city street in the
early evening. Slight film grain. No people anywhere in the frame, no hands, no faces, no bodies, no
silhouettes. The subject sits in the upper two-thirds; the bottom third is calm and uncluttered so text can
sit over it. No text, no signage lettering, no Hangul, no letters, no numbers, no logos, no watermarks.
```

## 다운로드는 1024로 줄여서 저장한다

Gemini의 '원본 크기 다운로드'는 **2048x2048**을 준다. `make_cards.py`의 워터마크 트림은
`img.size == (1024, 1024)`일 때만 동작하므로, 2048 그대로 넣으면 **✦ 워터마크가 카드에 그대로 남는다.**
윈도우에는 `sips`가 없으니 Pillow로 줄인다.

다운로드가 파일로 떨어지기까지 클릭 후 8~15초가 걸린다. 그 전에 `~/Downloads` 를 훑으면
**직전 편의 남은 파일을 집어간다.** 최근 3분 안에 생성된 파일만 고르도록 막아 두고 쓸 것.

## 이 편에서 그림이 깨지는 지점 다섯

- **조리원이 병원 병실로 나온다.** 산후조리원은 **호텔에 가까운 방**이다. 의료 장비, 링거대,
  모니터, 튜브, 수술복이 들어오면 틀렸다. `hotel-like private room, no medical equipment, no IV stand,
  no monitors` 를 컷마다 박는다.

- **신생아 얼굴이 박힌다.** `content6` 신생아실 컷이 제일 위험하다. `the newborns are swaddled with
  their faces turned away from the camera or softly out of focus, no recognizable faces` 를 지우지 말 것.
  얼굴이 읽히면 재생성한다.

- **미역국이 일본 와카메 샐러드로 나온다.** 한국 산후 밥상은 **뽀얀 국물의 미역국 한 그릇, 흰쌀밥,
  나물 반찬 서너 접시, 스테인리스 수저**다. 초밥, 미소국, 젓가락받침이 나오면 틀렸다.
  `a bowl of Korean seaweed soup in clear broth, white rice, small side dishes` 로 못 박는다.

- **방이 일본식으로 나온다.** 다다미, 장지문이 나오면 틀렸다. 조리원 방은 **침대, 수유 쿠션,
  전기 포트, 벽걸이 에어컨, 블라인드 친 창**이다.

- **글자 있는 물건을 그리지 않는다.** 달력, 시계 문자판, 예약 장부, 휴대폰 화면은 전부 숫자와
  글자가 본체라 공통 블록과 정면 충돌한다. `content9`의 수첩은 **완전 백지**여야 하고,
  화면이 들어오는 컷은 **꺼진 검은 화면**으로만 쓴다.

---

아래가 장면 지시문이다. 재생성할 때는 해당 공통 블록을 이어 붙인다.

## hook.png — 복도를 걸어가는 산모 (시설-인물 블록)

병원도 집도 아닌 제3의 건물이라는 걸 한 장으로 세우는 컷이다. **호텔 복도처럼 보여야 한다.**

```
A woman in a soft robe and slippers walking away down the carpeted corridor of a modern Korean postpartum
care centre, seen from behind, one hand trailing on the wall, a small wheeled suitcase beside her. Warm
recessed ceiling lights, evenly spaced plain doors along the corridor, a low console table with a vase of
dried flowers. It reads as a quiet hotel, not a hospital — no medical equipment, no IV stand, no monitors,
no wheelchairs. No faces visible, no recognizable features, every door plate and sign a completely blank
surface. The lower third of the frame is empty carpet.
```

## content2.png — 조리원 방 (실내-무인 블록)

이름을 설명하는 장이다. **머무는 방**이라는 게 물건으로 보여야 한다.

```
A private room in a modern Korean postpartum care centre in the afternoon, a neatly made single bed with
a folded blanket, a crescent nursing pillow resting on it, a small side table with an electric kettle and
a covered cup, a wall-mounted air conditioner, a window with the blinds half drawn letting in soft daylight.
Wood-look flooring, a low armchair in the corner. Hotel-like, not clinical — no medical equipment, no IV
stand, no monitors. No people anywhere, no hands. Every label and panel is a completely blank surface. The
lower third of the frame is bare floor.
```

## content3.png — 미역국 상 (탑다운 손만 블록)

산후조리 규칙을 설명하는 장이다. **미역국 한 그릇이 주인공**이어야 한다.

```
Directly overhead view of a meal tray on a table in a Korean postpartum care centre, a white bowl of Korean
seaweed soup in a clear pale broth at the centre, a bowl of white rice beside it, four small side dishes of
seasoned vegetables, a stainless steel spoon and chopsticks laid on a folded napkin. One hand rests on the
tray edge, the other lifting the spoon. No sushi, no miso, no chopstick rests. Only hands and forearms
enter the frame, no faces, no heads, no shoulders. Warm overhead light. The lower third of the frame is
bare table surface.
```

## content4.png — 닫힌 현관 (실내-무인 블록)

삼칠일, 집을 닫아 두던 옛 관습의 장이다. 사람 없이 **닫힘**으로만 말한다.

```
The entrance hall of a Korean apartment photographed from inside looking at the closed steel front door,
mid-morning, a single pair of house slippers set neatly on the sunken entryway floor, a thin curtain drawn
across the small side window, daylight coming through it soft and diffused. Nothing else in the hall, no
shoes of visitors, no bags. No people anywhere, no hands, no silhouettes. The door and every surface is
completely blank with no lettering, numbers or notices. The lower third of the frame is empty hallway floor.
```

## stat.png — 개어 놓은 속싸개 (탑다운 손만 블록)

기간을 말하는 장이다. 달력도 시계도 쓰지 않고 **쌓인 천**으로 말한다.

```
Directly overhead view of a bed in a Korean postpartum care centre room, a tall neat stack of folded white
newborn swaddle cloths at the centre of a pale blanket, two hands smoothing the top cloth flat, a crescent
nursing pillow and a covered water cup at the edge of the frame. Plain white cloth with no pattern, no
printing and no embroidery. No calendar, no clock, no paper. Only hands and forearms enter the frame, no
faces, no heads, no shoulders. Soft window light. The lower third of the frame is bare blanket.
```

## content6.png — 신생아실 (시설-인물 블록)

이 편의 핵심 컷이다. **줄지어 놓인 아기 침대**가 한눈에 들어와야 한다.

```
The nursery of a Korean postpartum care centre seen from the doorway, a row of clear-sided bassinets on
wheels lined up under soft warm light, each holding a swaddled newborn, a staff member in a plain uniform
seen from behind leaning over the far bassinet. The newborns are swaddled with their faces turned away from
the camera or softly out of focus, no recognizable faces. Warm, calm and domestic rather than clinical —
no monitors, no tubes, no IV stands, no incubators. Every name card slot and panel is a completely blank
surface. The lower third of the frame is bare floor.
```

## content7.png — 새벽 3시의 집 침실 (실내-무인 블록)

다른 나라는 곧장 집으로 간다는 장이다. **혼자 감당하는 밤**이 사람 없이 보여야 한다.

```
A dim bedroom in an ordinary home at three in the morning, an unmade bed with the covers thrown back and
empty, a bassinet standing right beside it, a single small lamp on the floor casting a low warm pool of
light, the window black with night behind half-open curtains. A folded muslin cloth dropped on the bed. No
people anywhere, no hands, no silhouettes, and the bassinet is empty. Every surface is blank with no
lettering or numbers, any screen is switched off and completely black. The lower third of the frame is dim
floor.
```

## content8.png — 라운지의 두 사람 (시설-인물 블록)

조리원 동기가 생기는 장이다. **나란히 앉은 거리**가 전부인 컷이다.

```
The shared lounge of a Korean postpartum care centre in the afternoon, two women in matching soft robes
sitting side by side on a low sofa seen from behind, heads slightly turned toward each other
mid-conversation, each holding a paper cup. A potted plant beside the sofa, a wide window with sheer
curtains letting in pale daylight, another empty sofa further back. No faces visible, no recognizable
features, no medical equipment. Any screen in the frame is switched off and completely black. The lower
third of the frame is bare floor and the sofa base.
```

## content9.png — 백지 수첩과 펜 (탑다운 손만 블록)

회복을 예약한다는 장이다. 글자는 하나도 없이 **예약하는 몸짓**으로만 말한다.

```
Directly overhead view of a small desk at home, an open pocket notebook with completely blank cream pages
bearing no writing, no printing, no ruled lines and no numbers, a pen resting in the gutter, one hand
holding the page flat and the other hand resting beside a phone lying face down with its blank back upward.
A cup of barley tea and a folded pair of tiny newborn socks at the edge of the desk. Only hands and
forearms enter the frame, no faces, no heads, no shoulders. Warm desk light. The lower third of the frame
is bare desk surface.
```

## cta.png — 저녁의 건물 (실외-무인 블록)

계정 마무리 컷이다. 조용하고 넓게, 사람 없이 끝낸다.

```
A quiet Korean city street in the early evening photographed from the opposite pavement, a mid-rise
building with rows of windows lit warm yellow against a deep blue sky, a small landscaped planter and a
low hedge in the foreground, one white sedan parked at the kerb with a completely blank empty number plate.
No people anywhere, no figures in the windows. Every sign, banner and shopfront is a completely blank
surface with no writing, numbers or symbols. The lower third of the frame is dark empty pavement.
```
