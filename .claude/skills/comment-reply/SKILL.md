---
name: comment-reply
description: Write a reply to a comment a reader left on a What's Hot Korea post (Instagram, Facebook, Threads). Use when the user pastes a comment, asks 댓글 대응/답글, or asks how to answer a reader. Not for the first comment we post ourselves — that is the `reply` field in content/<date>.json.
---

# 댓글 답글

읽는 사람은 스크롤 중이다. **짧고, 먼저 공감하고, 질문으로 끝낸다.** 그게 전부다.
설명하고 싶어지면 그건 다음 카드뉴스 소재이지 답글이 아니다.

## 기본형

```
[공감 — 상대 말이 맞다고 인정] + [새 사실 한 개] + [짧은 질문]
```

- **2~3문장, 영어 300자 이내.** 넘으면 자른다. 문단 나누지 않는다.
- **마침표로 끝내면 대화가 끝나고, 물음표로 끝내면 대화가 시작된다.** 항상 물음표로.
- **상대가 쓴 단어를 그대로 되돌려 쓴다.** ("banking app" → "your bank app")
- **이모지는 문장당 최대 하나**, 그것도 공감 문장에만. 🙌 🫡 😅 정도. 없어도 된다.
- **감사 인사로 시작하지 않는다.** "Thanks for sharing!"은 자동응답처럼 읽힌다.
  바로 상대 얘기로 들어간다.
- 새 사실은 **하나만**. 두 개면 하나를 버린다.

## 유형별

| 댓글 | 답글 |
|---|---|
| "우리나라는 더 잘한다" | 먼저 맞다고 한다. 지지 않으려 하면 그 댓글창은 국가 대항전이 된다. 그 나라 고유명사 하나를 정확히 알고 있음을 보이고("Kaspi", "MyNumber"), 한국이 왜 그 모양인지를 한 문장으로 준 뒤 되묻는다 |
| 질문 | 답부터. 모르면 "모른다"가 정답이다. 지어내면 팩트체크 규칙 전체가 무너진다 |
| 정정 (우리가 틀림) | 즉시 인정하고 고맙다고 한다. 변명 금지. 카드가 틀렸으면 `content/<date>.json`의 fact_check에 남긴다 |
| 정정 (상대가 틀림) | "Actually..." 로 시작하지 않는다. 출처를 조용히 하나 대고 넘어간다 |
| 경험담·자기 나라 얘기 | 새 사실 없이 짧게 받고 한 번 더 물어도 된다. 이게 스레드를 살린다 |
| 단순 칭찬 | 답글 대신 좋아요. 답글은 반박·질문·정보 추가에만 쓴다 |
| 정치 유도, 인신공격, 혐오 | 답하지 않는다. 답글은 노출을 키운다. 숨김이 맞다 |

## 하지 말 것

- 한국 미화, 자기 비하, 방어. (카드뉴스 지침과 같다)
- 확인 안 된 숫자. 카드에 못 쓸 수치는 답글에도 못 쓴다
- 카드나 캡션에 이미 쓴 문장 반복. 답글은 새 정보 아니면 값이 없다
- 같은 스레드에서 같은 말 두 번
- 링크. 인스타에서 죽은 텍스트고 스팸으로 읽힌다

## 예시

> "In 🇰🇿 u can do get it all on a banking and a egov app on ur smartphone."

```
Kaspi carrying your documents is genuinely ahead of us 🙌 Korea only got its ID into KakaoTalk and Toss in 2025, and the kiosks survive because someone still wants the stamped paper. Does 🇰🇿 ever still ask you for paper?
```

공감 → 새 사실(2025년 모바일 신분증) → 짧은 질문. 213자.

## 답한 뒤

`comments/<발행일>.md`에 원문·답·근거를 남긴다. 형식은 `comments/README.md`.
같은 반박이 다음 편에도 온다 — 그때 다시 조사하지 않으려고 적어둔다.

## 근거

빠른 답글이 첫 몇 시간의 확산을 좌우하고(인스타는 활발한 댓글창을 신호로 읽는다),
짧은 답글이 긴 답글보다 반응이 좋다는 것, "공감 → 정보 한 개 → 질문" 구조가
업계 공통 권장형이라는 것은 여러 소셜 운영 가이드에서 반복되는 내용이다:
Buffer(답글이 참여도를 21% 올린다는 자체 데이터), NapoleonCat, Brandwatch(댓글 유형별
대응), Sculpt(브랜드 목소리의 일관성). 트롤에 답하지 않는 것도 공통이다.
