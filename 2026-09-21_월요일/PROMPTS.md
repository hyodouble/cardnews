# Gemini 이미지 프롬프트 — 2026-09-21 (명절 잔소리)

10장 전부 아래 지시문으로 생성한다. `assets/2026-09-21/`에 이 파일명으로 넣는다.

`hook.png` `content2.png` `content3.png` `content4.png` `stat.png` `content6.png`
`content7.png` `content8.png` `content9.png` `cta.png`

계정은 `hoohihi123123`(Gemini Pro), 이미지 모드(Nano Banana 2).
**컷마다 새 채팅을 연다.** 같은 채팅에서 다음 프롬프트를 넣으면 생성이 아니라 직전 이미지의
편집으로 처리된다. `https://gemini.google.com/u/1/images` 로 새로 열면 새 채팅 + 이미지 모드가
한 번에 잡힌다.

## 공통 블록은 넷이다

블록의 `People appear only from behind` 는 모델이 **사람을 넣으라는 지시로 읽는다.** 무인 컷에
인물 블록을 쓰면 배경에 사람이 깔리므로 컷 성격대로 나눠 쓴다. 이 편은 무인 컷이 둘이다.

**실내-인물용** — `hook`, `content6`, `content7`, `content8`, `content9`

```
Photorealistic documentary photograph, square 1:1 framing, shot indoors in a Korean apartment under warm
interior light. Slight film grain, shallow depth of field. The subject sits in the upper two-thirds of the
frame; the bottom third is calm and uncluttered so text can sit over it. People appear only from behind,
cropped at the shoulders, or blurred. No text, no signage lettering, no Hangul, no letters, no numbers, no
logos, no watermarks, no recognizable faces.
```

**탑다운 손만** — `content2`, `content4`, `stat`

```
Photorealistic documentary photograph, square 1:1 framing, shot from directly above a low table in a Korean
home. Slight film grain. Only hands and forearms enter the frame from the edges — no faces, no heads, no
shoulders, no bodies, no reflections of people. No text, no signage lettering, no Hangul, no letters, no
numbers, no logos, no watermarks.
```

**실내-무인용** — `content3`

```
Photorealistic documentary photograph, square 1:1 framing, shot indoors in a Korean apartment under warm
interior light. Slight film grain. No people anywhere in the frame, no hands, no faces, no bodies, no
silhouettes. The subject sits in the upper two-thirds; the bottom third is calm and uncluttered so text can
sit over it. No text, no signage lettering, no Hangul, no letters, no numbers, no logos, no watermarks.
```

**실외-무인용** — `cta`

```
Photorealistic documentary photograph, square 1:1 framing, shot outdoors in a Korean apartment complex in
the early evening. Slight film grain. No people anywhere in the frame, no hands, no faces, no bodies, no
silhouettes. The subject sits in the upper two-thirds; the bottom third is calm and uncluttered so text can
sit over it. No text, no signage lettering, no Hangul, no letters, no numbers, no logos, no watermarks.
```

## 다운로드는 1024로 줄여서 저장한다

Gemini의 '원본 크기 다운로드'는 **2048x2048**을 준다. `make_cards.py`의 워터마크 트림은
`img.size == (1024, 1024)`일 때만 동작하므로, 2048 그대로 넣으면 **✦ 워터마크가 카드에 그대로 남는다.**

```bash
sips -z 1024 1024 ~/Downloads/Gemini_Generated_Image_xxxx.png --out assets/2026-09-21/hook.png
```

다운로드가 파일로 떨어지기까지 클릭 후 8~15초가 걸린다. 그 전에 `~/Downloads` 를 훑으면
**직전 편의 남은 파일을 집어간다.** 최근 3분 안에 생성된 파일만 고르도록 막아 두고 쓸 것.

## 이 편에서 그림이 깨지는 지점 다섯

- **한국 거실이 일본 다다미방으로 나온다.** 이 편은 실내 컷이 여섯이라 제일 크게 걸리는 지점이다.
  한국 거실은 **장판이나 마루 바닥, 좌식 낮은 상, 방석, 벽걸이 에어컨, 베란다 창**이다.
  `vinyl or wood flooring, a low floor table with floor cushions, a sliding glass veranda door behind` 를
  컷마다 박는다. 다다미, 장지문, 로우 소파가 나오면 틀렸다.

- **명절 상차림이 중국·일본 상으로 나온다.** 한국 명절상은 **전 부침 접시, 반달 송편, 놋그릇 또는
  백자, 층층이 괸 사과와 배, 깎은 배 접시, 식혜잔**이다. `plates of pan-fried jeon, half-moon rice
  cakes, brass and white porcelain bowls, stacked apples and pears` 로 못 박는다. 초밥이나 만두
  찜통이 나오면 틀렸다.

- **봉투에 글자가 박힌다.** `stat` 컷의 흰 봉투는 **완전 백지**여야 한다. 모델은 봉투를 보면
  축의금 봉투처럼 한자나 한글을 새겨 넣는다. `a completely plain white envelope with no writing,
  no printing, no characters, no pattern` 을 지우지 말 것. 지폐는 절대 넣지 않는다 — 얼굴과 숫자가
  같이 들어와 공통 블록을 깬다.

- **앨범 사진면에 얼굴이 박힌다.** `content4` 는 앨범을 넘기는 컷이라 사진 속 얼굴이 들어오기 쉽다.
  `the photographs on the album pages are out of focus and indistinct, no recognizable faces, no legible
  writing` 을 넣어 둔 이유다. 얼굴이 읽히면 재생성한다.

- **잔소리 메뉴판 자체는 그리지 않는다.** 글자가 본체인 물건이라 공통 블록과 정면으로 충돌한다.
  `stat` 컷은 메뉴판 대신 **빈 봉투와 찻잔**으로 값을 말한다. 재생성할 때 메뉴판이나 가격표를
  다시 집어넣지 말 것.

---

아래가 장면 지시문이다. 재생성할 때는 해당 공통 블록을 이어 붙인다.

## hook.png — 상을 둘러싼 가족 (실내-인물 블록)

명절 저녁상이 곧 질문 자리라는 걸 한 장으로 세우는 컷이다. 대화 중인 몸짓이 보여야 한다.

```
A family gathered on the floor around a low table in a Korean apartment living room on a holiday evening,
seen from behind and slightly above, five or six people seated on floor cushions with their backs to the
camera, some leaning in toward each other mid-conversation. On the table are plates of pan-fried jeon,
half-moon rice cakes, a brass bowl of stacked apples and pears, small cups of sweet rice punch. Vinyl
flooring, a sliding glass veranda door glowing behind them. No faces visible, no recognizable features. The
lower third of the frame is bare floor and cushion edges.
```

## content2.png — 어른 손이 밀어주는 접시 (탑다운 손만 블록)

잔소리가 무엇인지 설명하는 장이다. 다그침이 아니라 **챙김의 몸짓**으로 읽혀야 한다.

```
Directly overhead view of a low table in a Korean home during a holiday meal, an older weathered hand
pushing a small plate of peeled and sliced Korean pear toward a younger hand resting beside a cup of sweet
rice punch. Around them, plates of pan-fried jeon, half-moon rice cakes and a brass bowl of stacked fruit.
Only hands and forearms enter the frame, no faces, no heads, no shoulders. Warm overhead light. The lower
third of the frame is bare table surface.
```

## content3.png — 현관에 줄지어 놓인 신발 (실내-무인 블록)

식구가 다 모였다는 장이다. 사람 없이 **켤레 수**로만 말해야 한다.

```
The entrance hall of a Korean apartment on a holiday, photographed from standing height looking down at the
sunken entryway, eight or nine pairs of shoes lined up neatly side by side in very different sizes — men's
dress shoes, worn trainers, small children's shoes, an elderly woman's flat shoes. A steel apartment door
closed behind them, warm light from the living room spilling in from the right. No people anywhere, no
hands, no legs. Every shoe is plain with no visible branding or lettering. The lower third of the frame is
empty hallway floor.
```

## content4.png — 앨범을 넘기는 손 (탑다운 손만 블록)

질문이 정해진 순서를 따라온다는 장이다. **지나온 단계**가 물건으로 보여야 한다.

```
Directly overhead view of an old family photo album open on a low table in a Korean home, thick pages with
corner-mounted snapshots, a hand turning one page while another hand rests flat on the facing page. The
photographs on the album pages are out of focus and indistinct, no recognizable faces and no legible
writing anywhere. A cup of barley tea and a plate of half-moon rice cakes sit at the edge of the table.
Only hands and forearms enter the frame, no faces, no heads, no shoulders. The lower third of the frame is
bare table surface.
```

## stat.png — 상 위의 빈 봉투 (탑다운 손만 블록)

질문에 값이 매겨졌다는 장이다. 메뉴판도 지폐도 쓰지 않고 **봉투 하나**로 말한다.

```
Directly overhead view of a low wooden table in a Korean home, a single completely plain white envelope
lying closed at the centre with no writing, no printing, no characters and no pattern on it, a cup of
barley tea beside it and a small plate of half-moon rice cakes to one side. One hand rests on the table
edge near the envelope, fingers relaxed, not touching it. No banknotes, no coins, no faces, no heads, no
shoulders. Warm overhead light, the lower third of the frame is bare table surface.
```

## content6.png — 몸을 기울인 어른 (실내-인물 블록)

호의가 감사로 들리는 순간이다. **거리와 시선의 방향**이 전부인 컷이다.

```
Inside a Korean apartment living room on a holiday evening, an older relative seen from behind leaning
across a low floor table toward a younger person whose back and shoulders are turned to the camera, the
rest of the family blurred in the background further down the room. The camera focuses on a cup of barley
tea in the foreground, both figures softly out of focus. Vinyl flooring, floor cushions, a sliding glass
veranda door behind. No faces visible, no recognizable features. The lower third of the frame is bare floor
and the table edge.
```

## content7.png — 베란다 창가에 선 한 사람 (실내-인물 블록)

일정표가 더 이상 맞지 않는다는 장이다. **한 사람과 나머지 방 사이의 거리**로 말한다.

```
A young adult standing alone at the sliding glass veranda door of a Korean apartment on a holiday evening,
seen from behind, shoulders relaxed, looking out at the lit windows of the facing apartment block. Deeper
in the room behind, the blurred backs of relatives seated around a low table under warm light. Vinyl
flooring, a floor cushion left empty near the door. No faces visible, no recognizable features, no legible
writing anywhere. The lower third of the frame is bare floor.
```

## content8.png — 부엌에서 설거지하는 두 사람 (실내-인물 블록)

다른 나라에서는 안부를 묻는다는 장이다. 상 위가 아니라 **옆에서 나누는 대화**여야 한다.

```
Two people standing side by side at the sink of a small Korean apartment kitchen after a holiday meal, both
seen from behind, one rinsing a brass bowl and the other drying plates with a cloth, heads slightly turned
toward each other mid-conversation. Stacked dishes and a steel pot on the counter, a rice cooker at the
edge of the frame with its panel blank and unlit. Warm overhead light. No faces visible, no recognizable
features, no branding or lettering on any appliance. The lower third of the frame is the plain counter
front.
```

## content9.png — 신발 신고 나가는 뒷모습 (실내-인물 블록)

명절이 짧은 방문으로 바뀌었다는 장이다. **머무는 그림이 아니라 떠나는 그림**이어야 한다.

```
The entrance hall of a Korean apartment in the evening, a person seen from behind crouching to put on their
shoes at the sunken entryway, a light shoulder bag and a wrapped food container set down beside them, the
steel front door already half open with cool blue evening light coming through. Warm living-room light
behind them from the right. No faces visible, no recognizable features, no lettering on the bag or the
container. The lower third of the frame is the empty hallway floor.
```

## cta.png — 불 켜진 아파트 동 (실외-무인 블록)

계정 마무리 컷이다. 조용하고 넓게, 사람 없이 끝낸다.

```
A Korean apartment complex at early evening photographed from the ground between two buildings, rows of
windows lit warm yellow against a deep blue sky, a few parked white and grey sedans along the kerb with
completely blank empty number plates, low landscaped shrubs in the foreground. No people anywhere, no
figures in the windows. Every sign, banner and parking marking is a completely blank surface with no
writing, numbers or symbols. The lower third of the frame is dark empty pavement.
```
