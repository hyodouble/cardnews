# cardnews 작업 규칙

하루 1편 카드뉴스를 Instagram·Threads·Facebook에 올리는 레포. 편 내용은 `content/<날짜>.json`, 렌더는 `make_cards.py`, 발행은 `run_day.sh`.

## 주제
- 새 편은 조사·작성 전에 주제 후보 2~3개를 한국어 한 줄씩 보여주고, 사용자가 고른 뒤에 진행한다. 혼자 정하고 검색부터 시작하지 않는다 (2026-11-12~).
- 후보를 내기 전에 `content/*.json` 본문까지 grep해서 중복을 확인한다.
- 방향: 귀여운 상식보다 나라 단위 제도·사회 주제. 외국인이 "그게 실제야?" 하고 자기 나라와 비교할 만한 것 (2026-10-15~). 근거: 2026-10-13 Threads 조회수, 수능 비행기 68k·산후조리원 50k vs 귀여운 상식 78~450.
- 후보 예: 대학 서열, 출산 정책, 휴대폰 실명제, 아파트 중심 주거.

## 발행 전 승인
- 새 편은 슬라이드·캡션·댓글을 한국어로 번역해 채팅에 모두 보여주고, 사용자가 허락한 뒤에만 발행한다. 사진·렌더는 기다리는 동안 해도 된다.
- 허락 전에는 `run_day.sh`(`--render-only` 제외)와 `publish_today.py`를 실행하지 않는다.
- 사용자가 "발행해"라고 해도 새 편이면 한 번 더 확인한다.

## 미리 발행 금지
- 오늘보다 날짜가 뒤인 편은 렌더·커밋·push까지만 한다. 사용자가 그 편을 지금 올리라고 명시할 때만 발행한다.
- 승인을 물을 때 발행 시점을 적는다 ("지금 바로 올림" / "내일"). "진행"은 준비해도 좋다는 뜻일 수 있다.
- 하루 1편. 2026-11-08에 다음 날 편을 바로 올렸다가 삭제한 일이 있다.

## Threads
- Threads 글·댓글에는 해시태그를 쓰지 않는다. `post.py`의 `fit_threads`가 제거한다.
- `content/<날짜>.json`의 `hashtags`는 그대로 둔다 (Instagram·Facebook 사용).
- 다른 방법으로 Threads에 올릴 때는 직접 태그를 뺀다.

## 첫 댓글(reply)
- `reply`는 영어만, 400자 이내 한 덩어리. 한국어 번역을 붙이지 않는다 (2026-09-19~).
- 캡션·해시태그는 원래 영어. 슬라이드 한국어판(`DESIGN.md`)은 별개.

## 역할 분담
- Claude: 주제 내용과 사진 프롬프트(`content/<날짜>.json`, `photo_prompts`) 작성.
- 이미지 생성·저장(`assets/<날짜>/<key>.png`)은 Codex 담당. 이후 Claude가 이미지를 검수(정사각형, 키와 슬라이드 일치)하고 `make_cards.py`로 렌더한다.
- `codex exec`에는 이미지 도구가 없어 Mac Chrome의 Gemini를 쓴다. `assets/<날짜>/CODEX_TASK.md`를 쓰고 `codex exec -s workspace-write -C ~/cardnews "Follow assets/<날짜>/CODEX_TASK.md exactly." < /dev/null`을 백그라운드로 실행한다. `< /dev/null`이 없으면 stdin 대기로 멈춘다.
- Codex 한도가 소진됐으면 Claude가 Chrome으로 직접 만든다.
