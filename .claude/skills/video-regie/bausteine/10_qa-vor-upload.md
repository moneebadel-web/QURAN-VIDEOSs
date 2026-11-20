# 10 QA vor dem Upload

Nichts geht an Karim, bevor alles hier grün ist. Ergebnis als kurze Liste mitschicken.

## Technik (automatisch)
- `ffprobe`: 1080×1920, fps, Dauer, Größe < 25 MB (IG).
- Lautheit: `ffmpeg -i out.mp4 -af loudnorm=print_format=json -f null -` → -14 ±1 LUFS, TP ≤ -1 dBTP.
- `blackdetect=d=0.1`, `freezedetect=n=0.003:d=0.5` (außer gewollte Standbilder), `silencedetect=n=-45dB:d=0.6` (lange Löcher im Ton).
- A/V-Sync: Ausgabe-Ton gegen Sprachspur an 3 Stellen kreuzkorrelieren, Abweichung konstant und < 40 ms.

## Bild (ansehen)
- Kontaktbogen: `ffmpeg -i out.mp4 -vf "fps=2,scale=216:-1,tile=8x6" -frames:v 1 sheet.jpg`, plus Einzelbilder an jedem Grafik-Einstieg.
- Frame 1 zeigt den Hook. Nichts auf Gesicht/Kopf. Untertitel nie zwei Zeilen übereinander, kommen 0,08 s vor dem Wort.
- Safe-Zone-Overlay (09) auf 3 Frames. Loop-Naht: letzter und erster Frame nebeneinander.
- Arabisch: von rechts nach links, Buchstaben verbunden, Zahlen richtig herum.

## Inhalt
- Rechtschreibung DE/AR/EN in allen Texten im Bild und in der Caption.
- `werberecht-finanzberater`: kein "unabhängig" ohne Honorarberatung, keine Garantien, Risikohinweis wenn nötig.
- CTA-Wort im Video und in der Caption identisch.
