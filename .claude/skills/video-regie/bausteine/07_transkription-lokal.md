# 07 Transkription: Wort-Zeitstempel für Schnitt und Untertitel

## Was wo geht
- Deutsch im Container: Autoschnitt-Pipeline (`/mnt/project-files/knowledge/autoschnitt/`, sherpa-onnx + Parakeet von GitHub-Releases).
- Arabisch: Parakeet kann kein Arabisch, und Hugging-Face-/Whisper-Downloads sind im Container gesperrt (nie umgehen). Darum:
  - Weg 1: Karim gibt den Skripttext (aus 06), Abgleich per Forced Alignment wie im `yalla-reel-editor`.
  - Weg 2: whisper.cpp auf Karims Laptop über eine Remote-Control-Sitzung.

## whisper.cpp auf dem Laptop (Windows)
1. Release-ZIP `whisper-bin-x64` von github.com/ggml-org/whisper.cpp/releases entpacken.
2. Modell `ggml-large-v3-turbo.bin` (≈1,6 GB, einmalig) in `models\` legen.
3. `ffmpeg -i video.mov -ar 16000 -ac 1 -c:a pcm_s16le audio.wav`
4. `whisper-cli -m models\ggml-large-v3-turbo.bin -f audio.wav -l ar -ml 1 -ojf -of audio`
   (`-l de` für Deutsch, `-ml 1` = ein Wort pro Segment, `-ojf` = JSON mit Zeitstempeln).
5. `audio.json` zurück ins Projekt, daraus die Wortliste bauen.

## Qualität
- Ägyptischer Dialekt wird nicht perfekt erkannt: immer mit Skripttext gegenlesen, Zahlen und Fachwörter (ETF, Trade Republic) prüfen.
- Zeitstempel auf ±40 ms prüfen: Untertitel kommen 0,08 s vor dem Wort.
