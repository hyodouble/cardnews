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
A medium shot from behind and slightly to one side of an adult sitting cross-legged on a
heated wooden floor in a Korean sauna, seen from the shoulders up, photographed from a few
steps back so the head sits in the upper middle of the frame with space on both sides and
nothing cropped at the edges. On the head is a white bath towel worn as the Korean sauna
'yangmeori': a soft rounded bonnet of towelling that drapes over the crown and the whole
back of the head down to the nape, loose and slightly puffy, not tight, not a balaclava,
the neck and shoulders bare of it. At each side of the head the end of the towel is wound
into a compact tight spiral knot, like a small cinnamon roll or a coiled snail shell seen
end-on, so the spiral coil faces sideways out of the frame. Each spiral is about fist-sized
and sits at temple height at the side of the head, resting just above the ear and slightly
covering the top of it, sticking straight out sideways. Two spirals, one on each side,
symmetrical. Not pointed, not standing upright, not ears, not horns, not pompoms.
The person wears a loose muted salmon-orange cotton t-shirt. Face not visible. Soft warm
indoor light, background a blurred wooden wall.
```

**이 장은 세 번 틀리고 네 번째에 맞았다. 프롬프트를 손보기 전에 실제 사진부터 볼 것.**
`찜질방 양머리 수건`으로 이미지 검색을 하면 바로 나온다. 글로 된 접는 법 설명만 읽고
쓰면 계속 어긋난다 — 실제로 그렇게 어긋났다.

틀렸던 순서와 이유:

1. `two upright horns` → 수건 끝이 위로 뾰족하게 선 토끼귀. 양머리는 뿔이 아니다.
2. `cylindrical rolls` → 옆에 붙긴 했는데 굵은 원통이 되었고 위치가 너무 뒤였다.
3. 뒤통수까지 덮게 했더니 목까지 내려오는 복면이 되었다.

실물은 이렇다. **수건 본체는 정수리와 뒤통수를 덮는 부드러운 보닛**이고 목은 드러난다.
양쪽 끝은 굵은 원통이 아니라 **달팽이처럼 촘촘히 감긴 나선**이라 옆에서 소용돌이 단면이
보인다. 그 나선이 **관자놀이~귀 높이에서 옆으로 튀어나와 귀 윗부분을 살짝 덮는다.**
`spiral`, `cinnamon roll`, `temple height`, `just above the ear` 넷이 핵심이고
`not horns`, `not pompoms`를 같이 넣어야 다시 뿔로 돌아가지 않는다.

거리도 프롬프트에 박아 둘 것. 클로즈업으로 뽑으면 12% 트림 뒤 나선 한쪽이 잘린다.

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

**실사진 한 장을 레퍼런스로 첨부하고** 아래를 붙여넣는다. 공통 규칙은 아래에 녹아 있으니
따로 붙이지 않는다. 레퍼런스는 `assets/2026-09-05/content9-reference.png`.

```
Use the attached photo as the reference for WHAT is in the picture, not for how it is lit.
Recreate the same subject as a photorealistic documentary photograph, square 1:1 framing,
contemporary South Korea.

Keep from the reference, exactly: a dark brown plastic cafeteria tray; on the left a round
white ceramic dish holding four roasted Korean sauna eggs with matte tan-brown shells
mottled with darker scorch patches, ordinary egg shape, no speckles or dots; on the right
two identical clear cylindrical plastic tubs of sikhye, the Korean sweet rice drink, each
with a bright blue screw-on lid with a hinged blue flip tab standing open, one yellow
plastic straw through the near tub's lid. The drink is pale milky beige with soft cooked
white rice grains suspended through it, condensation on the outside of the tubs. The tubs
are completely plain with no printing, no labels.

Change the setting and the light: instead of a bright tiled floor under fluorescent light,
place the tray on the warm wooden floor of a dim Korean sauna lounge, shot at floor level
from a few steps back. Muted warm-neutral color grade, slight film grain, shallow depth of
field, one warm overhead light. Background is blurred dark wood only, empty, no furniture,
no chairs, no doorways.

The tray sits in the upper two-thirds of the frame and the bottom third is plain empty
floor so text can sit over it. No people, no hands. No text, no signage, no Hangul, no
letters, no numbers, no logos, no brand marks, no watermarks.
```

글로만 쓴 프롬프트로는 두 번 다 틀렸다. 세 번째에 실사진을 레퍼런스로 붙였다.

- **용기** — 처음엔 `파란 스냅 뚜껑 통`, 다음엔 `투명 텀블러`로 썼는데 둘 다 반찬통이나
  카페 컵이 나왔다. 실물은 **손잡이 없는 원통형 투명 통에 파란 나사 뚜껑**이고 뚜껑에
  **경첩식 플립 탭**이 서 있고 **노란 빨대**가 꽂혀 있다. 이건 글로 재현이 안 돼서
  사진을 붙이는 쪽이 빠르다.
- **계란** — `speckled shells`로 쓰면 점박이 메추리알 같은 구가 나온다. 맥반석 계란은
  점이 없다. **무광 황갈색에 거뭇한 얼룩**, 모양은 그냥 달걀이다. 흰 접시에 네 알.
- **레퍼런스의 조명은 쓰지 않는다.** 실물 사진은 형광등 아래 타일 바닥이라 나머지
  아홉 장의 어두운 나무 톤과 안 맞는다. 프롬프트에서 피사체만 가져오고 배경과 빛은
  갈아끼우라고 명시해야 한다.

`make_cards.py`의 12% 워터마크 트림은 이제 1024x1024 (제미나이 출력)에만 걸린다.
실사진에는 ✦ 표시가 없는데 트림이 들어가면 오른쪽 통이 잘려 나갔다.

## cta.png — 새벽의 빈 복도

```
An empty warm-lit corridor inside a 24-hour Korean sauna building in the small hours,
wooden floor stretching away, low doorways on one side, a folded towel left on a bench.
Nobody in frame. Quiet warm light, the lower part of the frame plain floor.
```
