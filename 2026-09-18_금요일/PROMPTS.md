# Gemini 이미지 프롬프트 — 2026-09-18 (눈치)

10장 전부 아래 지시문으로 생성한다. `assets/2026-09-18/`에 이 파일명으로 넣는다.

`hook.png` `content2.png` `content3.png` `content4.png` `stat.png` `content6.png`
`content7.png` `content8.png` `content9.png` `cta.png`

계정은 `hoohihi123123`(Gemini Pro), 이미지 모드(Nano Banana 2).
**컷마다 새 채팅을 연다.** 같은 채팅에서 다음 프롬프트를 넣으면 생성이 아니라 직전 이미지의
편집으로 처리된다. `https://gemini.google.com/u/1/images` 로 새로 열면 새 채팅 + 이미지 모드가
한 번에 잡힌다.

## 공통 블록은 넷이다

블록의 `People appear only from behind` 는 모델이 **사람을 넣으라는 지시로 읽는다.** 무인 컷에
인물 블록을 쓰면 배경에 사람이 깔리므로 컷 성격대로 나눠 쓴다. 이 편은 무인 컷이 셋이다.

**실내-인물용** — `hook`, `content3`, `content6`, `content8`

```
Photorealistic documentary photograph, square 1:1 framing, shot indoors in Korea under warm interior light.
Slight film grain, shallow depth of field. The subject sits in the upper two-thirds of the frame; the bottom
third is calm and uncluttered so text can sit over it. People appear only from behind, cropped at the
shoulders, or blurred. No text, no signage lettering, no Hangul, no letters, no numbers, no logos, no
watermarks, no recognizable faces.
```

**실내-무인용** — `content4`, `stat`

```
Photorealistic documentary photograph, square 1:1 framing, shot indoors in Korea. Slight film grain, shallow
depth of field. No people anywhere in the frame, no hands, no faces, no bodies, no silhouettes. The subject
sits in the upper two-thirds; the bottom third is calm and uncluttered so text can sit over it. No text, no
signage lettering, no Hangul, no letters, no numbers, no logos, no watermarks.
```

**탑다운 손만** — `content2`, `content7`, `content9`

```
Photorealistic documentary photograph, square 1:1 framing, shot from directly above a table indoors in Korea.
Slight film grain. Only hands and forearms enter the frame from the edges — no faces, no heads, no shoulders,
no bodies, no reflections of people. No text, no signage lettering, no Hangul, no letters, no numbers, no
logos, no watermarks.
```

**실외-인물용** — `cta`

```
Photorealistic documentary photograph, square 1:1 framing, shot outdoors in a Korean neighbourhood in the
evening. Slight film grain, shallow depth of field. The subject sits in the upper two-thirds; the bottom
third is calm and uncluttered so text can sit over it. People appear only from behind, cropped at the
shoulders, or blurred. No text, no signage lettering, no Hangul, no letters, no numbers, no logos, no
watermarks, no recognizable faces.
```

## 다운로드는 1024로 줄여서 저장한다

Gemini의 '원본 크기 다운로드'는 **2048x2048**을 준다. `make_cards.py`의 워터마크 트림은
`img.size == (1024, 1024)`일 때만 동작하므로, 2048 그대로 넣으면 **✦ 워터마크가 카드에 그대로 남는다.**

```bash
sips -z 1024 1024 ~/Downloads/Gemini_Generated_Image_xxxx.png --out assets/2026-09-18/hook.png
```

다운로드가 파일로 떨어지기까지 클릭 후 8~15초가 걸린다. 그 전에 `~/Downloads` 를 훑으면
**직전 편의 남은 파일을 집어간다.** 최근 3분 안에 생성된 파일만 고르도록 막아 두고 쓸 것.

## 이 편에서 그림이 깨지는 지점 다섯

- **주제가 '분위기'라서 그릴 게 없다.** 눈치는 물체가 없는 소재다. 추상으로 가면 스톡사진이 되므로
  **전부 회식·회의·카페 같은 구체적 자리**로 내렸다. 재생성할 때 장면을 추상화하지 말 것.

- **얼굴이 제일 큰 위험이다.** 이 편은 사람 컷이 많고, 표정이 곧 주제라 모델이 얼굴을 넣고 싶어한다.
  인물 컷은 **뒤통수 또는 어깨 아래 크롭**을 장면 지시문에 다시 박았다. 그래도 얼굴이 들어오면
  재생성보다 **더 먼 구도로 바꾸는 편이 싸다**(2026-09-15 편에서 확인).

- **메뉴판·화이트보드·모니터는 전부 글자 자리다.** 공통 블록의 `no letters` 하나로는 진다.
  종이·화면·판이 나오는 컷은 컷마다 **'완전 백지' 또는 '읽을 수 없게 블러'**를 다시 박는다.
  아래 지시문에 이미 들어가 있으니 지우지 말 것.

- **한국 회식 테이블이 서양 식당으로 나온다.** 한국 상은 **가운데 불판이나 찌개 냄비, 스테인리스
  수저·앞접시, 작은 초록 소주병, 낮은 유리잔**이다. `a portable gas burner in the middle, stainless
  steel spoons and chopsticks, small green soju bottles, small glass tumblers` 로 못 박는다.
  와인잔·빵접시·큰 냅킨이 나오면 틀린 것이다.

- **한국 사무실이 서양 오피스로 나온다.** 낮은 파티션, 좁은 통로, 형광등, 모니터 두 대, 책상마다
  머그컵이다. `low partitions, narrow aisles, fluorescent ceiling tubes` 를 붙인다.

---

아래가 장면 지시문이다. 재생성할 때는 해당 공통 블록을 이어 붙인다.

## hook.png — 아무도 말하지 않는 회의실 (실내-인물 블록)

"눈치가 없다"는 말이 나오기 직전의 방이다. 한 사람만 자세가 어긋나 있는 게 그림의 전부다.

```
A small Korean meeting room photographed from just inside the door, four people seated around a plain
rectangular table seen strictly from behind and from the side, every one of them cropped at the shoulders or
turned away so no face is visible. Three of them sit leaning slightly back with their hands still on the
table; one at the near end leans forward with an arm raised mid-gesture, clearly out of step with the
others. A whiteboard on the far wall is completely blank with nothing written or drawn on it, notebooks on
the table are closed and unprinted. Low partitions visible through the glass wall behind, fluorescent
ceiling tubes, pale grey carpet. The lower third of the frame is bare table edge and empty chair backs.
```

## content2.png — 회식상 위의 손들 (탑다운 손만 블록)

눈치를 '읽는 순간'을 사람 없이 그린다. 잔이 멈춰 있고 손만 여섯이다.

```
Directly overhead view of a Korean restaurant table mid-meal, a portable gas burner with a shallow stew pot
bubbling in the middle, small side dishes in white bowls arranged around it, stainless steel spoons and
chopsticks on paper rests, small green soju bottles and small glass tumblers. Six hands and forearms enter
from the edges of the frame, all of them paused and still: one hand resting flat beside a glass, one holding
chopsticks just above a dish without taking anything, one with fingers around an untouched tumbler. No
faces, no heads, no shoulders, no bodies anywhere. Every bottle label and every printed surface is left
completely blank. Warm overhead light, the lower third of the frame is bare table surface.
```

## content3.png — 말이 끊긴 카페 자리 (실내-인물 블록)

영어에 대응어가 없다는 장을, 말로 못 옮기는 순간으로 그린다. 두 사람, 둘 다 뒷모습이다.

```
Two people sitting across a small café table beside a window, both seen strictly from behind and cropped at
the shoulders so neither face is visible, one of them mid-sentence with a hand slightly lifted, the other
completely still with both hands around a mug. Two coffee cups, one half empty. The window beyond them is
bright and blown out, the street outside blurred past reading with all signage out of focus. Plain wooden
table, no printed menu, no paper on the table, no lettering on the cups. Warm indoor light against cold
window light. The lower third of the frame is bare table and the back of one chair.
```

## content4.png — 아무도 앉지 않은 상석 (실내-무인 블록)

자리를 정해주는 사람이 없는데 자리가 정해져 있다. 그래서 사람을 다 빼고 세팅만 남긴다.

```
A long private dining room table in a Korean restaurant photographed from one end before anyone has sat
down, completely empty of people. Places set evenly down both sides with stainless steel spoons and
chopsticks, small white bowls and short glass tumblers, a portable gas burner set at intervals along the
middle. At the far end, one seat has a wider chair with its back to the wall and a clear view of the door;
the seat nearest the camera is a plain stool with its back to the doorway. Sliding paper-panelled doors
closed behind, warm low pendant lights. No people anywhere, no hands, no silhouettes through the panels.
Every surface bare of printing and labels. The lower third of the frame is empty polished table.
```

## stat.png — 아무 소리도 없는 방 (실내-무인 블록)

숫자 0이 올라가는 배경이다. 말해지지 않은 것이 요점이라 가장 비운다.

```
An empty Korean meeting room photographed head on, completely free of people: a plain table with chairs
pushed in at even angles, a large whiteboard on the far wall left entirely blank with no writing, no marks
and no marker tray contents, pale grey carpet, fluorescent ceiling tubes overhead. Cold flat even light with
no strong shadows. Nothing on the table at all, no paper, no cups, no devices, no lettering or labels on any
surface. No one in the frame, no silhouettes through the glass. The lower third of the frame is bare empty
table stretching toward the camera.
```

## content6.png — 어른 뒤에 선 아이 (실내-인물 블록)

글자보다 먼저 배운다는 장이다. 아이가 어른들을 지켜보는 구도로 간다.

```
A child of about six standing slightly behind and to the side of a group of seated adults at a family
gathering in a Korean home, the child seen strictly from behind and cropped at the shoulders so no face is
visible, head turned toward the adults as if watching them. The adults are seated on the floor around a low
table, all of them blurred and seen from behind or in profile past reading, none facing the camera. Floor
cushions, a low wooden table with small dishes, a patterned wall in soft focus. Warm evening indoor light.
No lettering on any surface. The lower third of the frame is bare floor between the child and the table.
```

## content7.png — 백지 메뉴판 하나 (탑다운 손만 블록)

"아무거나 시켜"가 나온 직후다. 메뉴판은 글자 자리이므로 완전히 백지로 못 박는다.

```
Directly overhead view of a restaurant table with a single open menu lying flat in the middle of the frame,
its pages completely blank white with no printing, no photographs, no lines and no characters of any kind.
Two hands enter from the top edge, one resting on the open page without pointing at anything, the other
holding a small glass of water. A stack of closed identical blank menus sits pushed to one side. Stainless
steel spoons and chopsticks set at two places, a plain white teapot. No faces, no heads, no bodies anywhere.
Warm overhead light, the lower third of the frame is bare table surface.
```

## content8.png — 상사가 일어날 때까지 (실내-인물 블록)

눈치야근이다. 불은 다 꺼졌는데 자리는 차 있는 사무실로 그린다.

```
A Korean open-plan office late in the evening with most of the ceiling lights switched off, photographed
from the back of the floor looking down a narrow aisle between low partitions. Three people remain at their
desks, every one of them seen strictly from behind and cropped at the shoulders so no face is visible, each
lit only by their own monitors. Every monitor screen is a plain blank glow with no interface, no windows, no
icons and no text. One desk near the far corner is brightly lit with a lamp still on and a suit jacket over
the chair back. Dark windows along the far wall. The lower third of the frame is dark empty aisle floor.
```

## content9.png — 비기 전에 채워지는 잔 (탑다운 손만 블록)

눈치가 빠른 쪽의 장점이다. 잔이 비기 전에 병이 먼저 온다.

```
Directly overhead view of a Korean dining table, a hand entering from the left holding a small green bottle
tilted over a short glass tumbler that is still a third full, pouring into it, the other hand supporting the
pouring forearm at the wrist in the two-handed manner. A second hand enters from the right resting flat on
the table beside its own glass, not reaching for anything. Small side dishes in white bowls around them,
stainless steel chopsticks on a paper rest. No faces, no heads, no shoulders, no bodies anywhere. Every
bottle label left completely blank. Warm low light, the lower third of the frame is bare table surface.
```

## cta.png — 퇴근길 골목 (실외-인물 블록)

마무리 컷이다. 사람은 뒷모습 하나면 된다.

```
A narrow Korean neighbourhood alley in the evening after rain, two people walking away from the camera side
by side, seen strictly from behind and cropped at the shoulders so no face is visible. Low brick and tiled
buildings on both sides, a scooter parked against a wall, air conditioning units and tangled overhead
cables. Warm shop light spills onto the wet ground from the right but every sign and shopfront is blurred
well past reading with no legible lettering anywhere. The lower third of the frame is wet empty alley
pavement reflecting the light.
```
