# Gemini 이미지 프롬프트 — 2026-09-23 (반찬)

10장 전부 아래 지시문으로 생성한다. `assets/2026-09-23/`에 이 파일명으로 넣는다.

`hook.png` `content2.png` `content3.png` `content4.png` `stat.png` `content6.png`
`content7.png` `content8.png` `content9.png` `cta.png`

계정은 `hoohihi123123`(Gemini Pro), 이미지 모드. 이 계정은 이 컴퓨터에서 `/u/2` 다.
`https://gemini.google.com/u/2/images` 로 새로 열면 새 채팅 + 이미지 모드가 한 번에 잡힌다.
**컷마다 새 채팅을 연다.** 같은 채팅에서 다음 프롬프트를 넣으면 생성이 아니라 편집으로 처리된다.

새 채팅을 연 직후 **첫 입력은 입력창에 들어가지 않는다.** 클릭하고 타이핑해도 빈 채로 남으므로,
화면을 확인하고 **한 번 더 타이핑해야** 글자가 들어간다. 2026-09-22 편에서 매 컷마다 재현됐다.

## 공통 블록은 셋이다

블록의 `People appear only from behind` 는 모델이 **사람을 넣으라는 지시로 읽는다.** 무인 컷에
인물 블록을 쓰면 배경에 사람이 깔리므로 컷 성격대로 나눠 쓴다. 이 편은 탑다운이 여섯이다.

**탑다운 손만** — `hook`, `content2`, `content3`, `content4`, `stat`, `content6`

```
Photorealistic documentary photograph, square 1:1 framing, shot from directly above a table in a Korean
restaurant. Slight film grain. Only hands and forearms enter the frame from the edges — no faces, no heads,
no shoulders, no bodies, no reflections of people. No text, no signage lettering, no Hangul, no letters, no
numbers, no logos, no watermarks.
```

**실내-무인용** — `content7`, `content8`, `content9`

```
Photorealistic documentary photograph, square 1:1 framing, shot indoors in a small Korean restaurant under
warm light. Slight film grain. No people anywhere in the frame, no hands, no faces, no bodies, no
silhouettes. The subject sits in the upper two-thirds; the bottom third is calm and uncluttered so text can
sit over it. No text, no signage lettering, no Hangul, no letters, no numbers, no logos, no watermarks.
```

**실외-무인용** — `cta`

```
Photorealistic documentary photograph, square 1:1 framing, shot outdoors on a Korean restaurant street in
the early evening. Slight film grain. No people anywhere in the frame, no hands, no faces, no bodies, no
silhouettes. The subject sits in the upper two-thirds; the bottom third is calm and uncluttered so text can
sit over it. No text, no signage lettering, no Hangul, no letters, no numbers, no logos, no watermarks.
```

## 다운로드는 1024로 줄여서 저장한다

Gemini의 '원본 크기 다운로드'는 **2048x2048**을 준다. `make_cards.py`의 워터마크 트림은
`img.size == (1024, 1024)`일 때만 동작하므로, 2048 그대로 넣으면 **✦ 워터마크가 카드에 그대로 남는다.**

```bash
python grab.py 2026-09-23 hook
```

`grab.py`가 `~/Downloads`의 최신 Gemini 파일을 1024로 줄여 `assets/<날짜>/`에 넣고 원본을 지운다.
3분보다 오래된 파일은 거부한다 — 이미지가 다 그려지기 전에 다운로드 버튼을 누르면 아무 파일도
떨어지지 않고, 그때 이전 편의 남은 파일을 집어가는 사고가 난다.

**다운로드 버튼은 이미지 오른쪽 위 세 아이콘 중 맨 오른쪽이다.** 왼쪽은 공유(공개 링크 생성),
가운데는 클립보드 복사다. 09-22 편에서 왼쪽을 눌러 공개 링크 생성이 시작된 적이 있다.

## 이 편에서 그림이 깨지는 지점 다섯

- **한국 상이 일본·중국 상으로 나온다.** 제일 크게 걸리는 지점이다. 한국 반찬상은 **스테인리스
  작은 종지와 흰 도자기 접시, 납작한 스테인리스 젓가락과 긴 숟가락, 스테인리스 물컵**이다.
  초밥, 간장 종지 하나에 젓가락받침, 대나무 찜통, 붉은 회전 테이블이 나오면 틀렸다.

- **반찬이 샐러드로 나온다.** 반찬은 **배추김치, 무생채, 콩나물, 시금치나물, 어묵볶음, 감자조림,
  멸치볶음** 같은 것이다. 생채소 샐러드 그릇, 드레싱, 포크가 보이면 틀렸다.

- **병과 포장에 로고가 박힌다.** 초록 소주병과 라벨 붙은 물병은 글자가 본체라 공통 블록과 충돌한다.
  `no bottles, no packaging, no labels` 를 넣어 두었다. 스테인리스 물주전자와 컵으로만 간다.

- **셀프 반찬바가 뷔페 레스토랑으로 나온다.** `content8`은 **스테인리스 각통이 박힌 낮은 대와 집게**
  하나면 된다. 열선 램프, 접시탑, 유리 가림막이 줄줄이 선 호텔 뷔페가 나오면 틀렸다.

- **stat 컷에 숫자가 새겨진다.** 빈 종지와 채워진 종지 두 개로만 말한다. 영수증, 메뉴판, 가격표를
  절대 넣지 말 것 — 재생성할 때도 다시 집어넣지 말 것.

---

아래가 장면 지시문이다. 재생성할 때는 해당 공통 블록을 이어 붙인다.

## hook.png — 상 가득 깔린 반찬 (탑다운 손만 블록)

주문 전에 상이 찬다는 걸 한 장으로 세우는 컷이다. **접시 개수가 곧 훅**이다.

```
Directly overhead view of a small restaurant table in Korea covered edge to edge with ten small side
dishes in shallow stainless steel bowls and white porcelain plates — napa cabbage kimchi, seasoned bean
sprouts, spinach, stir-fried fish cake, braised potato, dried anchovies, pickled radish. Two hands are
setting down two more dishes at the top edge of the frame. Flat stainless steel chopsticks and long spoons
rest on paper napkins, a stainless water cup beside them. No bottles, no packaging, no labels, no menus, no
receipts. Only hands and forearms enter the frame, no faces, no heads, no shoulders. Warm overhead light.
The lower third of the frame is bare table surface.
```

## content2.png — 반찬 종지 클로즈업 (탑다운 손만 블록)

이름을 설명하는 장이다. **작은 종지 하나하나**가 또렷하게 읽혀야 한다.

```
Directly overhead close view of five small Korean side dishes in shallow stainless steel bowls grouped
together on a worn restaurant table — red napa cabbage kimchi, pale seasoned bean sprouts, dark green
spinach, orange stir-fried fish cake, glossy braised potato. A hand enters at the edge with flat stainless
steel chopsticks lifting a single strand of bean sprout. No salad greens, no dressing, no forks, no
bottles, no labels. Only hands and forearms enter the frame, no faces, no heads, no shoulders. Warm
overhead light. The lower third of the frame is bare table surface.
```

## content3.png — 다시 채워진 종지 (탑다운 손만 블록)

무료 리필을 말하는 장이다. **막 내려놓는 동작**이 보여야 한다.

```
Directly overhead view of a Korean restaurant table where a hand is setting down a freshly refilled
stainless steel bowl of kimchi, heaped and glistening, next to an emptied bowl of the same size holding
only a trace of sauce. Other side dishes and a bowl of white rice sit around them. No bill, no receipt, no
menu, no bottles, no labels anywhere. Only hands and forearms enter the frame, no faces, no heads, no
shoulders. Warm overhead light. The lower third of the frame is bare table surface.
```

## content4.png — 한 상 전체 (탑다운 손만 블록)

코스가 없다는 장이다. **밥·국·반찬이 동시에 놓인 한 사람 몫**이어야 한다.

```
Directly overhead view of one person's full Korean meal set on a restaurant table, all of it served at
once: a lidded stainless steel bowl of white rice, a hot stone bowl of soup beside it, a grilled mackerel
on a white plate, and seven small side dishes arranged in an arc around them. Flat stainless steel
chopsticks and a long spoon on a napkin. Two hands rest at the table edge, not holding anything. No
bottles, no packaging, no labels, no menu. Only hands and forearms enter the frame, no faces, no heads, no
shoulders. Warm overhead light. The lower third of the frame is bare table surface.
```

## stat.png — 빈 종지와 채워진 종지 (탑다운 손만 블록)

값이 0이라는 장이다. 영수증도 가격표도 쓰지 않고 **그릇 두 개**로 말한다.

```
Directly overhead view of a worn Korean restaurant table with exactly two small stainless steel bowls side
by side at the centre: the left one completely empty and clean, the right one heaped full of red napa
cabbage kimchi. A hand rests flat on the table beside them, relaxed. Nothing else on the table but a folded
paper napkin and a pair of flat stainless steel chopsticks. No money, no coins, no receipt, no menu, no
price tag, no bottles, no labels. Only hands and forearms enter the frame, no faces, no heads, no
shoulders. Warm overhead light. The lower third of the frame is bare table surface.
```

## content6.png — 김치 한 접시 (탑다운 손만 블록)

김치가 상수라는 장이다. **한 접시만 크게** 잡는다.

```
Directly overhead close view of a single white porcelain plate of freshly cut napa cabbage kimchi at the
centre of a worn wooden restaurant table, deep red and glossy, the cut edges of the cabbage clearly
visible. A hand at the frame edge holds flat stainless steel chopsticks just above the plate. Nothing else
in frame but the bare table and a folded napkin. No bottles, no jars, no labels, no lettering. Only hands
and forearms enter the frame, no faces, no heads, no shoulders. Warm overhead light. The lower third of the
frame is bare table surface.
```

## content7.png — 주방의 깨끗한 빈 그릇 (실내-무인 블록)

재사용 금지, 리필은 주방에서 나온다는 장이다. 사람 없이 **새 그릇**으로만 말한다.

```
The stainless steel prep counter of a small Korean restaurant kitchen, stacks of clean empty small
stainless steel side-dish bowls lined up ready, a large covered container of kimchi and a pair of tongs
beside them, a metal ladle hanging above. Everything clean, bright and orderly under overhead light. No
people anywhere, no hands. No packaging, no labels, no lettering on any container or appliance. The lower
third of the frame is the plain counter front.
```

## content8.png — 셀프 반찬바 (실내-무인 블록)

집게를 손님이 든다는 장이다. **낮은 대에 박힌 각통과 집게** 하나면 끝난다.

```
A self-serve side dish station at the side of a small Korean restaurant, a low counter with six
rectangular stainless steel inserts set into it holding different side dishes, a pair of tongs resting on
each, a stack of small empty plates at one end and a stainless water dispenser beside it. Plain tiled wall
behind. Not a hotel buffet — no heat lamps, no glass sneeze guard, no towers of plates. No people anywhere,
no hands. Every sign and label surface is completely blank. The lower third of the frame is the plain
counter front.
```

## content9.png — 저녁 식당 안 빈 자리 (실내-무인 블록)

공짜가 어려워지고 있다는 장이다. **조용하고 한산한 가게**로 말한다.

```
The interior of a small Korean restaurant in the evening with no customers, four square tables with
stainless steel chopstick drawers set into their sides, plastic chairs tucked in, a wall-mounted fan and a
water dispenser in the corner, warm light from a single ceiling fixture. One table still holds a stack of
clean empty side dish bowls. No people anywhere, no hands. Every menu board, sticker and sign is a
completely blank surface with no writing or numbers. The lower third of the frame is bare floor.
```

## cta.png — 저녁 식당 골목 (실외-무인 블록)

계정 마무리 컷이다. 조용하고 넓게, 사람 없이 끝낸다.

```
A narrow Korean restaurant alley in the early evening, low buildings on both sides with warm light spilling
from their windows onto the pavement, a folded sandwich board and a few stacked plastic crates outside one
door, a deep blue sky above the rooftops. No people anywhere, no figures in the windows. Every sign,
banner, awning and board is a completely blank surface with no writing, numbers or symbols. The lower third
of the frame is dark empty pavement.
```
