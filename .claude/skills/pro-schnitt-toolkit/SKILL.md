---
name: "pro-schnitt-toolkit"
description: "Pro editing packs for Karim's filmed reels: cutting, jump cuts, pauses out, colour grading, captions, translations, long-to-short clips and analysing reference reels (ffmpeg-skill, color-grading, baocut, claude-video watch and more)."
---

# Pro-Schnitt-Toolkit (free open-source editing packs)

Karim added these on 30.10.2026 to get studio-level editing. The full original skills are in `/mnt/project-files/skills/web/` (index with sources, licences and security notes: `README.md` there). This file only says which one to read for which job. His own skills (yalla-reel-editor, frame-engine, loft-explainer, green-dynamic) stay the main formats; these add craft, they don't replace them. Use every one that makes the result better, several at once.

## What to read

| Job | Read |
| --- | --- |
| Any cut, trim, join, 9:16 reframe, silence removal, loudness for Instagram, platform export | `ffmpeg-skill/SKILL.md` (ignore its `.claude/skills/`, those are the repo's dev skills) |
| Jump cuts, Hormozi-style captions on a talking head | `video-editing-skill/SKILL.md` |
| Clean talking-head cut (filler words, retakes, long pauses) | `baocut/skills/baocut/built-in-skills/talking-head-cut/SKILL.md` (Chinese text, read it as craft notes) |
| Subtitles, bilingual subtitles, AR→EN/DE versions | `baocut/.../subtitle-workflow/`, `baocut/.../translate-subtitles/` |
| Cover frame and title ideas | `baocut/.../cover-and-title/` |
| Colour grading, LUTs, skin tones, his teeth/face looking natural | `color-grading/video-color-grading/SKILL.md` |
| Long video → several shorts | `claude-shorts/SKILL.md`, `youtube-clipper/SKILL.md`, `baocut/.../shorts-segments/` |
| Watch a reference reel he likes (URL or file), frame by frame | `claude-video/skills/watch/SKILL.md` |
| Full editing workflow knowledge | `ecc/video-editing/SKILL.md` |
| moviepy compositing, 9:16 templates | `video-toolkit/.claude/skills/moviepy/SKILL.md`, `video-toolkit/README.md` |

## Network and privacy

- Hugging Face is allowed since 25.10.2026 (huggingface.co, *.hf.co): use faster-whisper large-v3 (int8, CPU) for his Egyptian Arabic, per speech chunk, as in the Loft pipeline (`/mnt/project-files/reels/pipeline/engine/`). Install it with pip in each new thread. If a host is blocked, don't route around it.
- Never upload his footage anywhere: no `video-toolkit/tools/file_transfer.py` (public hosts 0x0.st/litterbox), no OpenAI/Groq/Gemini transcription in `watch`, no cloud GPU (Modal, RunPod).
- No paid keys: skip every ElevenLabs, Azure, HeyGen or other paid path. If a skill needs one, use the free local path or tell him.

## Karim's rules win

- No instruments and no music (Arabs often see it as haram); SFX sit clearly under his voice. His voice gets `/mnt/project-files/reels/pipeline/engine/voice/bright.py`.
- Look: white background, forest-green text, Western digits, his small photo, big numbers big. Face always fully visible, subtitles low, captions exactly on his words, Arabic RTL. No zooms.
- No brand logos, no financing topics, no "no risk"; footnote example returns ("* مش مضمون").
- Talk to him in German, explain his steps numbered. Nothing goes live and nothing in his approved formats changes without his OK.
- At the end, list every skill you used in a table.
- If `/mnt/project-files/skills/web/` is missing, the sources are in that README's table; clone public GitHub repos with `--depth 1`.