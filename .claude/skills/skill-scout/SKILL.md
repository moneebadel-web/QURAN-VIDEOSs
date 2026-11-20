---
name: "skill-scout"
description: "Run at the start of every task with Karim (after video-regie/content-regie): search skills worldwide (skills.sh, GitHub, Anthropic directory) for ones that would clearly improve the result, and suggest the best free ones."
---

# Skill-Scout (based on vercel-labs/skills "find-skills", MIT)

Goal: before each task, check whether a skill exists somewhere in the world that makes the result clearly better than what Karim already has installed. Suggest it. Never install it without his OK.

## Order with his other skills
1. video-regie (videos) or content-regie (everything else) runs FIRST and loads all INSTALLED skills that fit.
2. skill-scout runs right after: it only looks for what is MISSING. If the installed skills already cover every part of the task (cut, motion, captions, sound, hook, text), say so in one line and do not search.
3. Then the task goes on with the installed skills. A new skill is only used after Karim said OK and saved it.

## How to search (in this order, stop when good hits are found)
1. Anthropic directory: the SuggestSkills / SearchSkills tools with keywords from the task.
2. skills.sh leaderboard and search. In the cloud skills.sh is often blocked by the network policy, so use WebSearch with queries like `skills.sh <task keywords>` or `"npx skills add" <keywords>`, and the mirrors mcpservers.org/agent-skills, skillselion.com, vibeindex.ai.
3. GitHub: `gh api -X GET search/repositories -f q='<keywords> SKILL.md'` and `search/code -f q='filename:SKILL.md <keywords>'`.
4. Optional, only if npm and skills.sh are reachable: `npx -y skills find <keywords>` (read-only search, never `skills add` without his OK).

Use 2-3 keyword sets per task, e.g. for a talking reel: "captions arabic", "talking head edit", "short-form retention".

## Quality filter (all must hold)
- Free and with a clear licence (MIT, Apache-2.0, CC0). No licence or noncommercial = drop.
- Popular: prefer 1,000+ installs; under 100 installs or a repo under 100 stars only with a clear reason.
- Trusted source first: anthropics, vercel-labs, microsoft, HeyGen, Remotion, then well-known authors.
- Read the SKILL.md and its scripts before suggesting: no paid API keys, no logins, no uploads of his videos or data to unknown servers, no telemetry left on.
- Must not break his fixed rules: no background music, no financing topics, no "ohne Risiko", no brand logos, his voice speed untouched in talking videos.
- Clearly better than what is installed (name the installed skill it beats and why). Duplicates are dropped.

## Report to Karim (German, short, step by step)
- Max 3 suggestions, best first, as a numbered list: name, what it improves in THIS task, installs, licence, source link, cost (free first).
- If nothing useful exists: one line "Keine bessere Skill gefunden, wir arbeiten mit den installierten weiter."
- Never interrupt the task for it: give the suggestion, keep working with the installed skills.

## After his OK
- Copy the full original pack to /mnt/project-files/skills/web/<name>/ with its licence and add a row to /mnt/project-files/skills/web/README.md.
- Write a small router skill for it (like web-video-toolkit or pro-schnitt-toolkit) and offer it on a propose_skills card so he can save it with one tap.
- Note it in project memory (web-skill-packs).

## Do not search again
- If the same kind of task had a search in the last 7 days, reuse that result instead of searching again.
- In the end-of-task skills table, list skill-scout with what it found (or "nichts Neues").