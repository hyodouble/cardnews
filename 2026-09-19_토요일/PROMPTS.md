# Gemini 이미지 프롬프트 — 2026-09-19 (귀성길 대이동)

10장 전부 아래 지시문으로 생성한다. `assets/2026-09-19/`에 이 파일명으로 넣는다.

`hook.png` `content2.png` `content3.png` `content4.png` `stat.png` `content6.png`
`content7.png` `content8.png` `content9.png` `cta.png`

계정은 `hoohihi123123`(Gemini Pro), 이미지 모드(Nano Banana 2).
**컷마다 새 채팅을 연다.** 같은 채팅에서 다음 프롬프트를 넣으면 생성이 아니라 직전 이미지의
편집으로 처리된다. `https://gemini.google.com/u/1/images` 로 새로 열면 새 채팅 + 이미지 모드가
한 번에 잡힌다.

## 공통 블록은 넷이다

블록의 `People appear only from behind` 는 모델이 **사람을 넣으라는 지시로 읽는다.** 무인 컷에
인물 블록을 쓰면 배경에 사람이 깔리므로 컷 성격대로 나눠 쓴다. 이 편은 무인 컷이 넷이다.

**실외-무인용** — `hook`, `content3`, `stat`, `content9`

```
Photorealistic documentary photograph, square 1:1 framing, shot outdoors in Korea. Slight film grain. No
people anywhere in the frame, no hands, no faces, no bodies, no silhouettes. The subject sits in the upper
two-thirds; the bottom third is calm and uncluttered so text can sit over it. No text, no signage lettering,
no Hangul, no letters, no numbers, no logos, no watermarks.
```

**실내-인물용** — `content4`, `content6`, `content7`

```
Photorealistic documentary photograph, square 1:1 framing, shot indoors in Korea under warm interior light.
Slight film grain, shallow depth of field. The subject sits in the upper two-thirds of the frame; the bottom
third is calm and uncluttered so text can sit over it. People appear only from behind, cropped at the
shoulders, or blurred. No text, no signage lettering, no Hangul, no letters, no numbers, no logos, no
watermarks, no recognizable faces.
```

**탑다운 손만** — `content2`, `content8`

```
Photorealistic documentary photograph, square 1:1 framing, shot from directly above a table in Korea.
Slight film grain. Only hands and forearms enter the frame from the edges — no faces, no heads, no shoulders,
no bodies, no reflections of people. No text, no signage lettering, no Hangul, no letters, no numbers, no
logos, no watermarks.
```

**실외-인물용** — `cta`

```
Photorealistic documentary photograph, square 1:1 framing, shot outdoors in a Korean village in the early
evening. Slight film grain, shallow depth of field. The subject sits in the upper two-thirds; the bottom
third is calm and uncluttered so text can sit over it. People appear only from behind, cropped at the
shoulders, or blurred. No text, no signage lettering, no Hangul, no letters, no numbers, no logos, no
watermarks, no recognizable faces.
```

## 다운로드는 1024로 줄여서 저장한다

Gemini의 '원본 크기 다운로드'는 **2048x2048**을 준다. `make_cards.py`의 워터마크 트림은
`img.size == (1024, 1024)`일 때만 동작하므로, 2048 그대로 넣으면 **✦ 워터마크가 카드에 그대로 남는다.**

```bash
sips -z 1024 1024 ~/Downloads/Gemini_Generated_Image_xxxx.png --out assets/2026-09-19/hook.png
```

다운로드가 파일로 떨어지기까지 클릭 후 8~15초가 걸린다. 그 전에 `~/Downloads` 를 훑으면
**직전 편의 남은 파일을 집어간다.** 최근 3분 안에 생성된 파일만 고르도록 막아 두고 쓸 것.

## 이 편에서 그림이 깨지는 지점 다섯

- **도로 컷은 전부 글자밭이다.** 고속도로 표지판, 요금소 요금 표시, 역 전광판, 차 번호판이 다
  글자 자리다. 공통 블록의 `no letters` 하나로는 진다. 컷마다 **표지판은 완전 백지, 번호판은 빈 판,
  전광판은 읽을 수 없게 블러**를 다시 박는다. 아래 지시문에 이미 들어가 있으니 지우지 말 것.

- **한국 고속도로가 미국 인터스테이트로 나온다.** 한국 도로는 **양옆 초록 방음벽, 좁은 갓길,
  뒤로 겹쳐 보이는 산 능선, 흰색·회색 세단과 SUV 위주**다. `green noise barriers along both sides,
  low forested mountain ridges behind, mostly white and grey sedans and SUVs` 로 못 박는다.
  픽업트럭이 줄줄이 나오거나 사막 지형이면 틀린 것이다.

- **차례상이 중국·일본 상차림으로 나온다.** 한국 명절상은 **놋그릇 또는 백자, 층층이 괸 사과와 배,
  전 부침 접시, 반달 모양 송편**이다. `brass and white porcelain bowls, stacked apples and pears,
  plates of pan-fried jeon, half-moon rice cakes` 를 붙인다. 초밥·만두찜통이 나오면 틀렸다.

- **휴게소가 미국 다이너로 나온다.** 한국 휴게소는 **야외 주차장, 스테인리스 쟁반, 종이컵,
  일회용 젓가락, 우동 그릇**이다. 부스 좌석과 두꺼운 머그컵이 나오면 틀렸다.

- **정체 컷은 붉은 테일라이트 띠가 전부다.** 낮 정체로 그리면 그냥 주차장 사진이 된다.
  `hook` 과 `content3` 은 해 진 뒤로 고정했다. 재생성할 때 낮으로 되돌리지 말 것.

---

아래가 장면 지시문이다. 재생성할 때는 해당 공통 블록을 이어 붙인다.

## hook.png — 여덟 차선이 다 서 있다 (실외-무인 블록)

3천만이 동시에 움직인다는 말을 한 장으로 세우는 컷이다. 차가 아니라 **띠**로 보여야 한다.

```
An eight-lane Korean motorway at dusk photographed from a high overpass looking straight down the road,
every lane in both directions packed solid with stationary cars, the outbound side a continuous river of red
tail lights stretching to the horizon. Green noise barriers run along both sides, low forested mountain
ridges behind, mostly white and grey sedans and SUVs. Every overhead gantry sign is a completely blank
panel with no writing, arrows or symbols, and every number plate is an empty blank plate. No people
anywhere, no figures between the cars. The lower third of the frame is dark empty asphalt in the foreground.
```

## content2.png — 송편 빚는 손 (탑다운 손만 블록)

명절이 무엇인지 설명하는 장이다. 사람 없이 손과 상차림만으로 한국 명절이라고 읽혀야 한다.

```
Directly overhead view of a low wooden table in a Korean home during holiday preparation, a wide tray of
half-moon rice cakes in white and pale green, a bowl of sesame filling, a plate of pan-fried jeon, stacked
apples and pears in a brass bowl to one side. Four hands and forearms enter from the edges, shaping a rice
cake, pressing a filled one closed, reaching toward the tray. No faces, no heads, no shoulders, no bodies
anywhere. Every package, wrapper and printed surface is left completely blank. Warm overhead light, the
lower third of the frame is bare table surface.
```

## content3.png — 서울을 빠져나가는 한쪽 (실외-무인 블록)

방향이 하나라는 장이다. **한쪽은 빨갛고 한쪽은 비어 있어야** 말이 된다.

```
A Korean motorway interchange at night photographed from directly above, the outbound carriageway a dense
unbroken band of red tail lights curving away from the city, the inbound carriageway almost empty with only
a few scattered white headlights. City tower blocks glowing in the distance behind, green noise barriers and
dark hillsides framing the road. Every overhead sign panel is completely blank with no lettering, arrows or
numbers, and every number plate is an empty blank plate. No people anywhere. The lower third of the frame is
dark roadside embankment.
```

## content4.png — 아홉 시간째 차 안 (실내-인물 블록)

네 시간이 아홉 시간이 된다는 장을 **차 안의 시간**으로 그린다. 앞유리 밖은 계속 정체다.

```
The inside of a family car during a long traffic jam, photographed from the back seat looking forward, the
driver and front passenger seen strictly from behind and cropped at the shoulders so no face is visible. A
child asleep against the far window in the back row, seen from behind. Through the windscreen a solid line
of stationary cars and red tail lights fades into evening haze. A holiday gift box and a folded blanket sit
on the seat beside the camera. The dashboard screen is a plain blank glow with no interface, no icons and no
text. Warm dim interior light. The lower third of the frame is the back seat and the gift box.
```

## stat.png — 열려 있는 요금소 (실외-무인 블록)

₩0 이 올라가는 배경이다. **차단기가 올라가 있고 부스가 비어 있는 것**이 요점이다.

```
A Korean motorway toll plaza photographed head on at dusk, completely empty of cars and people, every lane
barrier raised and every booth window dark and unattended. The overhead lane panels and the fare display
boards are completely blank surfaces with no numbers, no lettering and no symbols of any kind. Green noise
barriers and forested ridges behind the plaza, overhead lights just coming on. No people anywhere, no
silhouettes inside the booths. The lower third of the frame is empty lane asphalt running toward the camera.
```

## content6.png — 표가 사라진 아침 (실내-인물 블록)

기차표 이야기다. 사람은 뒷모습, 전광판은 블러. 승강장이 아니라 **대합실**이다.

```
The waiting hall of a large Korean railway station early in the morning, photographed from behind a row of
seated travellers, all of them seen strictly from behind or cropped at the shoulders so no face is visible,
several standing with suitcases and holiday gift boxes at their feet. A large departure board hangs above
them, blurred well past reading with no legible characters, numbers or symbols anywhere on it. High ceiling,
cold morning light through tall windows mixing with warm interior light. Every sign, poster and ticket
surface is blank or blurred past reading. The lower third of the frame is polished floor and luggage.
```

## content7.png — 그래도 간다 (실내-인물 블록)

교통 상황을 다 알면서도 가는 이유다. **도착한 뒤의 방**을 그려서 값을 치른 쪽을 보여준다.

```
A family gathering in a Korean home seen from the doorway, several relatives seated on the floor around a
low table spread with holiday dishes, every person seen strictly from behind, in profile or blurred so no
face is visible. An older relative sits at the far side with their back to the wall. Cushions on a warm
wooden floor, a sliding paper-panelled door half open behind them, coats and bags piled in the near corner
as if everyone has just arrived. Warm evening light. No lettering on any surface. The lower third of the
frame is bare floor and the pile of bags.
```

## content8.png — 새벽 휴게소 쟁반 (탑다운 손만 블록)

구체적인 장면 하나다. 아홉 시간짜리 운전의 중간 지점은 **새벽 휴게소 우동 한 그릇**이다.

```
Directly overhead view of a stainless steel tray on a motorway rest stop table late at night, a bowl of
noodle soup with steam rising, a paper cup of coffee, disposable wooden chopsticks on the tray, a paper
napkin, car keys set down beside it. Two hands enter from the edges, one holding the chopsticks over the
bowl, the other around the paper cup. No faces, no heads, no shoulders, no bodies anywhere. Every cup,
wrapper and packaging surface is left completely blank with no printing. Cold overhead fluorescent light on
the tray, the lower third of the frame is bare table surface.
```

## content9.png — 비어버린 서울 골목 (실외-무인 블록)

수도가 비고 지방이 찬다는 장이다. **평소 사람이 가득한 자리가 비어 있는 것**이 전부다.

```
A narrow Seoul commercial alley in the middle of the day, completely empty of people, both sides lined with
small shopfronts whose shutters are rolled down. Plastic stools stacked and chained beside a doorway, a
delivery scooter parked and covered, air conditioning units and tangled overhead cables above. Every sign,
shutter and shopfront surface is blank or blurred well past reading with no legible lettering anywhere.
Flat bright daylight with hard shadows. No people anywhere, no silhouettes in the windows. The lower third
of the frame is empty alley pavement.
```

## cta.png — 도착한 마당 (실외-인물 블록)

마무리 컷이다. 아홉 시간 뒤에 닿는 곳을 보여주고 끝낸다.

```
The yard of an old Korean village house in the early evening, two people walking away from the camera toward
the lit doorway carrying holiday gift boxes, both seen strictly from behind and cropped at the shoulders so
no face is visible. A car parked just inside the gate with its boot still open. Low tiled roof, a stone wall,
persimmon tree branches overhead, warm light spilling from the open door across the yard. Every surface is
free of lettering and the number plate on the car is an empty blank plate. The lower third of the frame is
bare swept yard ground.
```
