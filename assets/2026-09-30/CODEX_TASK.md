# Task: make 10 photos in Gemini via Chrome, save to assets/2026-09-30/

Use your Chrome browser tool (the user's real Mac Chrome). Do not use any image API or script.

Prompts: content/2026-09-30.json -> "photo_prompts". Keys in order:
hook, content2, content3, content4, stat, content6, content7, content8, content9, cta

Account: Gemini must run as the Google account "hihi hoo" (hoohihi123123). On this Mac that is
https://gemini.google.com/u/1/app . Confirm via the bottom-left avatar, not by guessing the URL.

For each key:
1. Open a NEW chat (https://gemini.google.com/u/1/app).
2. Switch to image mode, and set aspect ratio to 1:1 (menu items are [role=menuitemradio], label exactly "1:1").
   The default is 16:9 and it resets in each new chat.
3. Type the prompt as ONE line (no newlines). Focus first with
   document.querySelector('[contenteditable="true"]').focus()
4. Send by clicking button[aria-label="메시지 보내기"] via JS. Do NOT press Enter (it drops the prompt).
5. Wait until the image is done (40-70 s). Page decoration imgs are also 1024 wide, so judge completion
   by a new button[aria-label="원본 크기 이미지 다운로드"] appearing, not by img size.
6. Click that download button. The file lands in ~/Downloads/Gemini_Generated_Image_*.png.
   Chrome silently blocks the 2nd download in the same tab: use a new tab per download
   (open the chat URL in a fresh tab, download one image, close the tab).
7. Copy (cp, do not mv) that newest download to assets/2026-09-30/<key>.png immediately,
   before starting the next key, so file names can't drift.

After all 10: check each saved file is square (width == height) with python3 + PIL.
Do not edit any other file, do not commit or push.
Final answer: a list of key -> saved path -> pixel size, plus any key that failed.
