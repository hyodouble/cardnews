# 플러그인

터미널(로컬 Claude Code)에서 쓰던 개인 스킬을 계정에 붙여 다니게 만들기 위한 마켓플레이스다.
`~/.claude/` 아래 있는 것은 그 컴퓨터에만 있고, 클라우드 세션(앱/웹)에는 따라오지 않는다.
이 폴더에 담아 push하면 `/plugin marketplace add hyodouble/cardnews` 한 번으로 어디서든 쓸 수 있다.

## 채우는 법

1. PC에서 원본을 찾는다:
   `ls ~/.claude/skills ~/.claude/output-styles ~/.claude/agents | grep -i "caveman\|ponytail"`
2. 내용을 `plugins/<이름>/skills/<이름>/SKILL.md`에 붙여넣는다. frontmatter의
   `description`은 **언제 이 스킬이 켜져야 하는지**를 쓴다 — 이게 비면 영영 안 켜진다.
3. `plugins/<이름>/.claude-plugin/plugin.json`과 `.claude-plugin/marketplace.json`의
   TODO 설명을 채운다.
4. commit & push.

## 쓰는 법

```
/plugin marketplace add hyodouble/cardnews
/plugin install caveman@hyodouble
/plugin install ponytail@hyodouble
```

출력 스타일(`~/.claude/output-styles/`)이었다면 그대로 옮길 수 없다. 같은 내용을 스킬로
바꿔 담는 편이 이 환경에서는 확실하다.

나중에 카드뉴스 리포에서 떼어내고 싶으면 `.claude-plugin/`과 `plugins/`를 별도 리포로
옮기고 `/plugin marketplace add <새 리포>`로 바꾸면 된다.
