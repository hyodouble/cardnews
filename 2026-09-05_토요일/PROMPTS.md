# Gemini 이미지 프롬프트 — 2026-09-05 (찜질방)

10장. 파일명 그대로 `assets/2026-09-05/`에 저장할 것. 렌더러가 이 이름으로 찾는다.

`hook.png` `content2.png` `content3.png` `content4.png` `content5.png` `content6.png`
`content7.png` `stat.png` `content9.png` `cta.png`

## 공통 규칙 (모든 프롬프트 뒤에 붙임)

```
Photorealistic documentary photograph, square 1:1 framing, contemporary South Korea.
Muted warm-neutral color grade, slight film grain, shallow depth of field.
Subject sits in the upper two-thirds; the bottom third is calm and uncluttered so text can sit over it.
Everyone is fully clothed in the standard Korean sauna uniform: a loose muted salmon-orange cotton t-shirt and matching shorts, a few men in pale blue-grey. No nudity, no bathing scenes, no adults undressed, no children.
No text, no signage, no Hangul, no letters, no numbers, no logos, no brand marks, no watermarks, no recognizable faces.
```

목욕 구역은 한 장도 찍지 않는다. 인스타·제미나이 양쪽에서 걸리고, 카드가 설명하는
층은 어차피 옷 입고 있는 찜질 구역이다. 프롬프트마다 색을 박아 둘 것 — 찜질복은 보통 살구빛 주황이고, 남자용으로 옅은
청회색을 같이 두는 곳이 많다. 색을 빼면 회색 운동복이나 사우나 타월만 두른
그림이 나온다. 첫 hook 생성이 실제로 회색으로 나와서 프롬프트를 고쳤다.

실내 저조도라 광원을 장마다 하나씩 박아 뒀다. 빼면 인물이 뭉개진다.

---

## hook.png — 수면실 바닥

```
A wide dim room where a dozen adults lie asleep on thin mats on a heated wooden floor,
spaced apart, all in identical loose salmon-orange cotton t-shirts and shorts. Seen from the doorway
at floor height, bodies turned away, no faces visible. One low warm wall light.
```

## content2.png — 건물 안 복도

```
The interior corridor of a large 24-hour Korean sauna building at night: low arched
doorways to heated rooms along one side, warm wooden walls, a stack of folded towels
on a shelf. Empty of people. Warm ceiling downlights. Plain walls with no lettering.
```

## content3.png — 층이 갈리는 지점

```
A staircase inside a Korean bathhouse building, rising from a damp tiled lower landing
into a warm dry wood-floored lounge above. One adult in a salmon-orange cotton t-shirt and shorts walking
up, seen from behind. Cool light below, warm light above. No signboards, no lettering.
```

## content4.png — 양머리

```
A medium shot from behind and slightly to one side of an adult sitting on a heated wooden
floor in a Korean sauna, seen from the shoulders up and photographed from a few steps back,
so the head sits in the upper middle of the frame with generous empty space on both sides
and nothing cropped at the edges. On the head is a white bath towel folded in the Korean
sauna 'yangmeori' sheep-head style: folded lengthwise into a narrow band, both ends rolled
outward into two thick soft cylindrical rolls, like two rolled buns, sitting against the
sides of the head just above the ears, with the flat middle of the towel lying across the
top of the head. The rolls are rounded and chunky, never pointed, never standing upright.
The person wears a loose muted salmon-orange cotton t-shirt. Face not visible. Soft warm
indoor light, background a blurred wooden wall.
```

**양머리는 뿔이 아니다.** 첫 버전 프롬프트가 `two upright horns`였고, 그대로 수건 끝이
위로 뾰족하게 선 토끼귀가 나왔다. 실제 양머리는 수건을 길게 접어 **양 끝을 바깥으로
3~4번 말아** 두툼한 원통 두 개를 만들고, 가운데를 벌려 모자처럼 쓰는 것이다. 말린 롤이
귀 옆에 옆으로 붙어야 하고 위로 서면 안 된다. `rolled outward`, `cylindrical rolls`,
`never pointed`, `never standing upright` 넷 중 하나라도 빼면 다시 뿔이 나온다.

거리도 프롬프트에 박아 둘 것. 클로즈업으로 뽑으면 12% 트림 뒤 롤 한쪽이 화면 밖으로
잘린다. `from a few steps back` + `nothing cropped at the edges`가 그래서 들어가 있다.

## content5.png — 불가마

```
The inside of a Korean kiln sauna room: rounded clay and stone walls, a low arched
entrance, coarse jute mats on the floor, one adult in a salmon-orange cotton t-shirt and shorts lying curled
with their back to the camera. Dim orange glow from a single recessed lamp.
```

## content6.png — 목침과 매트

```
Floor-level close shot of a thin sleeping mat, a folded blanket and a hard wooden
headrest on a heated wooden floor, one adult asleep in the background out of focus in
a salmon-orange cotton t-shirt and shorts. Very low warm night lighting, no faces.
```

## content7.png — 공용 마루

```
A large warm common room in a Korean sauna: adults of different ages sprawled and
sitting on the wooden floor in identical salmon-orange cotton t-shirts and shorts, some lying down,
some leaning on cushions. Shot from the doorway, faces turned away or blurred.
Warm ceiling light. Blank walls with no lettering.
```

## stat.png — 문 닫은 동네 목욕탕

```
The exterior of a small old neighbourhood bathhouse building in a Korean back street
in daytime: pale tiled facade, a tall brick chimney behind it, roller shutter pulled
down, weeds at the base of the wall. Nobody in frame. Flat overcast light.
No signboards, no lettering, no symbols anywhere on the building.
```

## content9.png — 계란과 식혜

```
Floor-level shot of a small tray on a wooden sauna floor holding two boiled eggs still
in their shells and a plain bowl of pale sweet rice drink with grains floating in it.
Two hands reaching in from the edge of frame, sleeves of a salmon-orange cotton t-shirt.
Warm overhead light, no faces, no packaging, no labels.
```

## cta.png — 새벽의 빈 복도

```
An empty warm-lit corridor inside a 24-hour Korean sauna building in the small hours,
wooden floor stretching away, low doorways on one side, a folded towel left on a bench.
Nobody in frame. Quiet warm light, the lower part of the frame plain floor.
```
