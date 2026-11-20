---
name: "video-regie"
description: "Regie für jedes Video von Karim (Loft-Erklärvideo, Talking-Video, Reel, TikTok, DE/AR/EN): bindet automatisch alle passenden Skills, Bausteine und neuen Tools ein und listet am Ende alle benutzten Skills in einer Tabelle. Immer zuerst laden, wenn er ein Video will."
---

# Video-Regie

Karim erklärt nur, was er will. Er nennt keine Skills. Du entscheidest, welche Skills und Bausteine laufen, und nutzt ALLES, was das Video besser macht. Sprich mit ihm auf Deutsch, kurz und einfach.

## Schritt 0: Was steht heute zur Verfügung? (jedes Mal neu, in jedem Projekt)
Dieser Skill läuft in jedem von Karims Projekten (z. B. "Content" und dem Projekt mit dem Reel-Editor). Projektordner sind pro Projekt getrennt.
1. Arbeitsordner finden: Gibt es `/mnt/project-files/skills/video/` mit `REGISTER.md`, nimm den. Sonst lege ihn in DIESEM Projekt an (einmalig): `REGISTER.md` und `bausteine/01..10` aus dem Anhang unten als Dateien schreiben, die Assets mit dem Skript in Anhang C erzeugen. Ab dann gilt diese Kopie.
2. Lies `REGISTER.md` komplett.
3. Geh die Liste der Skills durch, die in dieser Sitzung verfügbar sind (Namen und Beschreibungen). Jeder Skill, der Video, Ton, Bild, Grafik, Untertitel, Hook, Caption, Musik, Schnitt, Thumbnail, Export, Recht oder Text betrifft, ist ein Kandidat, auch wenn er nicht im Register steht. Das ist der Hauptweg, wie neue Skills automatisch dazukommen.
4. Steht ein passender Skill oder ein neues Tool nicht im Register: nutze ihn trotzdem und trage ihn unter "Neu hinzugekommen" ein (Format siehe Register-Kopf).
5. Pfade aus anderen Skills (z. B. `/mnt/project-files/reels/pipeline/`) gibt es nur im Projekt, wo sie angelegt wurden. Fehlen sie, sag es Karim in einem Satz und arbeite mit den Bausteinen weiter.

## Schritt 1: Format wählen (genau eins trägt das Video)
- Erklärvideo, Animation, "Loft" → `loft-explainer` (+ `frame-engine`).
- Talking-Video Arabisch → `yalla-reel-editor`. Sagt er "green dynamic" → `green-dynamic`.
- Talking-Video Deutsch → Autoschnitt (`/mnt/project-files/knowledge/autoschnitt/ANLEITUNG.md`), Look nach Marke.
- Unklar → aus seiner Beschreibung die wahrscheinlichste Variante nehmen und das im ersten Satz sagen. Nur fragen, wenn es wirklich nicht erkennbar ist (einmal).
- Format-Skills, die Karim abgenommen hat ("perfekt"), haben Vorrang vor Bausteinen. Bausteine ergänzen, ersetzen aber nichts, was er freigegeben hat.

## Schritt 2: Ablauf (Bausteine aus `/mnt/project-files/skills/video/bausteine/ (bzw. Anhang A)` lesen, wenn sie dran sind)
1. Kein Skript da → 06 Skript & Teleprompter, mit `hooks-captions-offers`, `werberecht-finanzberater`, `text-humanisieren`.
2. Testbild oder Probe da, oder Rohmaterial schwach → 05 Dreh-Check (Tipps vor dem nächsten Dreh).
3. 07 Transkription (Wort-Zeitstempel).
4. 04 Retention-Schnitt: Retention-Tabelle (Zeit | gesagt | im Bild) vor dem Rendern.
5. 02 Farb-Look (gefilmtes Material), 03 Freistellen (wenn das Layout es braucht), 08 B-Roll (wenn Platz).
6. Grafik/Animation über das Format-Skill, ergänzt mit `web-video-toolkit` und `frame-engine`.
7. 01 Ton-Studio (Stimme, Musik, SFX).
8. 09 Export & Safe Zones, Titelbild (`canvas-design` / Feed-System), Caption + `hashtags-finden`.
9. 10 QA vor Upload. Erst wenn alles grün ist, an Karim schicken, mit 2 bis 3 Zeilen: was drin ist, was du geprüft hast.
10. Skill-Tabelle (Pflicht, bei jeder Lieferung): Am Ende der Nachricht mit dem fertigen Video eine Tabelle aller benutzten Skills und Bausteine, in der Reihenfolge des Einsatzes:

| Skill / Baustein | Wofür in diesem Video |
|---|---|
| yalla-reel-editor | Format: Talking-Reel AR |
| 01 Ton-Studio | Hall raus, -14 LUFS |
| ... | ... |

Darunter eine Zeile "Nicht benutzt:" mit passenden Skills, die bewusst weggelassen wurden, jeweils mit kurzem Grund (z. B. "08 B-Roll: kein Platz im 30-s-Video"). Neu entdeckte Skills mit "(neu)" markieren.
Wird die Antwort dadurch zu lang, kommt die Tabelle in eine Datei neben dem Video und wird mitgeschickt.

## Feste Regeln von Karim (gelten immer)
- Zooms und langsame Push-ins sind erlaubt (seit 30.10.2026), sparsam. Nichts auf Gesicht oder Kopf. Untertitel 0,08 s vor dem Wort, nie zwei Zeilen übereinander.
- Musik mit Instrumenten ist erlaubt, immer leise unter der Stimme. Der Hintergrund muss nicht weiß sein (30.10.2026).
- Untere 25 % frei (30.10.2026): ab y=1440 von 1920 nichts Wichtiges (keine Untertitel, Fußnoten, CTAs, Grafiken), weil Instagram/TikTok den Bereich verdecken. Untertitel etwa bei y=1350, Inhalt darüber.
- Branding in JEDEM Video, die ganze Zeit (30.10.2026): sein Foto, "Karim Adel", "yalla Finanzen", "Financial Consultant for Arabs & Expats in Germany" und +49 163 1549878. Klein und dezent oben (unter den 220 px der App-Leiste), sein Bild nicht zu groß: das Video anschauen hat Vorrang.
- Echte Federn für jede Bewegung, keine CSS-Animationen (frame-engine).
- Arabisch im ägyptischen Dialekt, von rechts nach links.
- Nur kostenlose Tools. Bezahl-Tools höchstens als Hinweis, nie als Voraussetzung.
- "unabhängig" nur, wenn Karim Honorarberatung bestätigt.
- Gesperrte Hosts nie umgehen; dann läuft es auf seinem Laptop (Remote Control) oder mit seinem Skripttext.
- Er will EINE fertige Version schnell; kleine Korrekturen in dieselbe Version.

## Ehrlich bleiben
Du schneidest über Code und siehst Videos als Einzelbilder und Transkript. Sag es, wenn Feinschliff nach Gefühl in CapCut schneller wäre, oder wenn die Aufnahme das Limit ist.

## Pflege
- Neuer video-relevanter Skill oder neues Tool (in jedem Thread) → Zeile in REGISTER.md.
- Karim gibt ein Ergebnis frei ("perfekt", "genau so") → als Format oder Regel ins Register bzw. in den passenden Baustein.
- Feste Regel geändert → hier unter "Feste Regeln" ändern und die Karte neu vorschlagen.

---
# Anhang A: Die 10 Bausteine
## 01 Ton-Studio: Stimme wie im Studio

Ziel: klare, warme Stimme, kein Hall, kein Rauschen, -14 LUFS, Musik immer unter der Stimme.
Wenn `/mnt/project-files/reels/pipeline/` da ist: dessen Kette (dereverb.py, sh.rnnn, music7.py, qa7.py) hat Vorrang, sie ist von Karim abgenommen.

### Messen zuerst
- Rauschboden: 2 s Stille aus dem Rohvideo, `ffmpeg -i in.wav -af astats -f null -` (RMS level). Über -50 dB = laut, RNNoise mit mix 0.95; unter -60 dB = mix 0.5 reicht.
- Hall: Ausklingen nach Satzende anhören bzw. mit `revstat.py` messen. Hörbarer Hall: erst Dereverb (WPE), dann die Kette.

### Standardkette (Sprache)
```
highpass=f=100,
arnndn=m=sh.rnnn:mix=0.95,
agate=threshold=0.015:ratio=3:release=120:range=0.12,
equalizer=f=120:t=h:w=1:g=1.5, equalizer=f=300:t=q:w=1:g=-4.5,
equalizer=f=3200:t=q:w=1:g=3.5, equalizer=f=9000:t=h:w=1:g=2.5,
deesser=i=0.45,
acompressor=threshold=-22dB:ratio=3:makeup=3,
loudnorm=I=-14:TP=-1.5:LRA=9
```
- loudnorm immer zweistufig: erster Lauf `print_format=json`, zweiter Lauf mit `measured_*`-Werten.
- Leise Wortenden (Gate/RNNoise frisst sie): Stelle vorher +9 dB anheben oder über einen leichteren Pfad (mix 0.5, ohne Gate) überblenden.
- Handy-Mikro mit viel Raum: Präsenz (+3 dB bei 3,2 kHz) eher weniger, sonst klingt es blechern.

### Musik und SFX
- Musik etwa 20 dB unter der Stimme, zusätzlich Ducking:
  `[musik][stimme]sidechaincompress=threshold=0.02:ratio=8:attack=20:release=300[m]`
- SFX (Whoosh, Pop, Klick) nur auf Bildwechsel und Zahlen, nie über ein Schlüsselwort. Quelle: synthetisierte SFX der Frame-Engine oder HyperFrames-SFX-Bibliothek (web-video-toolkit).
- Am Ende: `alimiter=limit=0.63:level=0:latency=1` (level immer 0). Ziel nach AAC: -14 ±1 LUFS, True Peak ≤ -1 dBTP.

### Prüfen
A/B-Schnipsel (roh vs. fertig, je 5 s) rendern und in QA (10) anhören bzw. messen.

## 02 Farb-Look: jedes Video gleich hochwertig

Ziel: gleicher Hautton und Look in allen Videos, egal ob Fenster- oder Lampenlicht.

### 1. HDR erkennen und auf SDR bringen
`ffprobe -v error -select_streams v:0 -show_entries stream=color_transfer,color_primaries -of csv=p=0 in.mov`
- `arib-std-b67` (HLG) oder `smpte2084` (PQ) = iPhone-HDR. Dann:
  `zscale=t=linear:npl=100,format=gbrpf32le,zscale=p=bt709,tonemap=hable:desat=0,zscale=t=bt709:m=bt709:r=tv,format=yuv420p`
- Danach Hautton prüfen: hable macht oft etwas flach, darum folgt Schritt 2.

### 2. Korrektur (pro Video, messen statt raten)
- Gesichtsbereich messen (MediaPipe face_landmarker oder Mitte oberes Drittel): Ziel-Luma Gesicht ≈ 0.55 bis 0.65, Rot > Grün > Blau, R−B ≈ 0.10 bis 0.18.
- Zu kühl: `colorbalance=rm=0.04:bm=-0.04`. Zu dunkel: `eq=gamma=1.08` (nicht brightness, das hebt Schwarz an).
- Grünstich (Leuchtstofflampe): `colorbalance=gm=-0.03`.

### 3. Look
`lut3d=/mnt/project-files/skills/video/assets/karim_warm.cube` (warm in den Mitten, leicht kühle Schatten, Hauttöne geschützt).
Stärke regeln: Look-Ebene mit `blend=all_mode=normal:all_opacity=0.7` über die korrigierte Ebene.
Look nur ändern, wenn Karim es sagt. Neue Looks als eigene .cube in `assets/` ablegen und hier eintragen.

### 4. Kontrolle
Ein Standbild vorher/nachher nebeneinander (`hstack`) ansehen: Haut natürlich, keine orangene Stirn, Weiß bleibt weiß.

## 03 Freistellen: Person sauber vom Hintergrund

Gebraucht für: Karten/Text hinter Karim, Split-Screen mit Kopf-Pop-out, Hintergrund abdunkeln.

### Weg A (Container): MediaPipe
- Modell `selfie_multiclass.tflite` aus `/mnt/project-files/reels/pipeline/models/` und `matte.py` aus `edit/`.
- Alpha = clip((0.75−bg)/0.4), danach Kanten: 2× Erosion, dann 3 px Weichzeichnen.
- Gegen Flackern: Alpha zeitlich glätten (EMA, 0.6 aktuell + 0.4 vorher), bei schnellen Bewegungen weniger glätten.
- Matte nach jeder Schnittänderung neu berechnen.

### Weg B (bessere Haare, läuft auf Karims Laptop): RobustVideoMatting
- Kostenlos (GPL-3.0, eigene Nutzung ok). ONNX-Modell `rvm_mobilenetv3_fp32.onnx` aus den GitHub-Releases von PeterL1n/RobustVideoMatting, Python mit onnxruntime.
- Im Container ist PyPI gesperrt, daher per Remote-Control-Sitzung auf dem Laptop ausführen und nur das Alpha-Video (ProRes 4444 oder PNG-Folge) zurückholen.

### Regeln
- Nie Text über Gesicht oder Kopf (Karims Regel).
- Vor dem Planen an 3 s testen: Kanten an Haaren und Händen ansehen (Kontaktbogen).
- Ohne gute Matte lieber Layout ohne Freistellen wählen als Kanten zeigen.

## 04 Retention-Schnitt: Leute bleiben bis zum Ende

Gilt für Talking-Videos und Loft-Erklärvideos.

### Erste 1,5 Sekunden
- Kein Hallo, kein Logo, kein Intro. Erstes Bild = Karim mitten im Hook-Satz oder die Hook-Grafik.
- Hook als Text oben im Bild schon ab Frame 1 (max. 7 Wörter), gleichzeitig gesprochen.
- Hook-Typen: Fehler ("Dieser Fehler kostet dich…"), Zahl ("7 € am Tag…"), Gruppe ("Ägypter in Deutschland…"), Gegenthese.

### Rhythmus
- Pausen > 0,25 s raus, 0,08 s Atem lassen. Füllwörter (äh, ähm) raus; bei Arabisch "يعني" nur raus, wenn der Satz ohne es gleich bleibt.
- Versprecher/Neuansätze: immer die letzte saubere Version nehmen.
- Alle 2 bis 4 s ein visueller Wechsel: Layoutwechsel, Textkarte, B-Roll, Zahl, Icon. Zooms/Push-ins sind seit 30.10.2026 erlaubt, sparsam einsetzen.
- Wichtigste Zahl oder Aussage bekommt die größte Grafik und einen SFX.

### Spannungsbogen
- Offene Schleife früh: "Punkt 3 ist der teuerste" o. ä. und erst am Ende auflösen.
- CTA erst nach dem Nutzen, kurz: "Kommentiere X". Kein Verkaufston.
- Loop-Ende: letzter Satz führt in den ersten zurück, letzter Frame passt zum ersten.

### Längen
Talking: 25 bis 50 s. Loft-Erklärvideo: 55 bis 75 s. Lieber kürzer und dichter.

### Plan vor dem Rendern
Eine Retention-Tabelle schreiben: Zeit | gesagt | was im Bild passiert. Lücke > 4 s ohne Wechsel = nachbessern.

## 05 Dreh-Check: gute Aufnahme vor gutem Schnitt

Karim schickt ein Testbild oder 10 s Probe. Antwort: höchstens 5 konkrete Punkte, wichtigster zuerst.

### Bild prüfen
- Licht: Fenster oder Lampe VOR ihm, leicht seitlich (45°). Gesicht nicht dunkler als Hintergrund. Gegenlicht = sofort umdrehen.
- Belichtung messen: Gesicht-Luma 0.55 bis 0.65, keine ausgefressenen Stellen auf Stirn.
- Kamera auf Augenhöhe, Augen im oberen Drittel, oben etwas Luft über dem Kopf (Untertitel und Hook brauchen Platz unten und oben).
- Hintergrund: 1 bis 2 m Abstand zur Wand, aufgeräumt, eine warme Lichtquelle hinten (Lampe) gibt Tiefe.
- iPhone: Hauptkamera (nicht Selfie-Kamera, wenn möglich), 4K 30 fps, AE/AF-Sperre durch langes Tippen, Linse putzen.

### Ton prüfen
- Ansteckmikro oder Handy nah (max. 50 cm). Rauschboden aus 2 s Stille messen (unter -55 dB gut).
- Hall: Klatschen in der Probe, Ausklingen anhören. Viel Hall = Teppich, Vorhang, Sofa, oder näher ans Mikro.

### Performance
- Erste 3 Wörter mit Energie, in die Linse schauen, nicht aufs Display.
- Pro Satz neu ansetzen ist ok, Schnitt räumt das auf (04).

## 06 Skript und Teleprompter für Talking-Videos

### Aufbau
1. Hook (1 Satz, max. 8 Wörter)
2. Warum es ihn betrifft (1 bis 2 Sätze)
3. Die 3 Punkte oder die eine Lösung, jeweils mit Zahl oder Beispiel
4. Auflösung der offenen Schleife
5. CTA: "Kommentiere X" (weich, Hormozi-Stil)

### Länge
Deutsch ≈ 2,5 Wörter/s, Ägyptisch-Arabisch ≈ 2,3 Wörter/s. 40 s ≈ 100 Wörter.

### Teleprompter-Fassung
- Zeilen mit max. 6 Wörtern, ein Gedanke pro Zeile, Leerzeile = Pause.
- Arabisch im ägyptischen Dialekt schreiben, wie er spricht, nicht Hocharabisch.
- Zusätzlich die reine Textfassung speichern: sie ist der Abgleichtext für Untertitel (siehe 07).

### Pflicht-Durchläufe
- Hooks und CTA mit `hooks-captions-offers`.
- Rechtlich mit `werberecht-finanzberater` (kein "unabhängig" ohne Honorarberatung, keine Renditeversprechen).
- Sprache mit `text-humanisieren`.

## 07 Transkription: Wort-Zeitstempel für Schnitt und Untertitel

### Was wo geht
- Deutsch im Container: Autoschnitt-Pipeline (`/mnt/project-files/knowledge/autoschnitt/`, sherpa-onnx + Parakeet von GitHub-Releases).
- Arabisch: Parakeet kann kein Arabisch, und Hugging-Face-/Whisper-Downloads sind im Container gesperrt (nie umgehen). Darum:
  - Weg 1: Karim gibt den Skripttext (aus 06), Abgleich per Forced Alignment wie im `yalla-reel-editor`.
  - Weg 2: whisper.cpp auf Karims Laptop über eine Remote-Control-Sitzung.

### whisper.cpp auf dem Laptop (Windows)
1. Release-ZIP `whisper-bin-x64` von github.com/ggml-org/whisper.cpp/releases entpacken.
2. Modell `ggml-large-v3-turbo.bin` (≈1,6 GB, einmalig) in `models\` legen.
3. `ffmpeg -i video.mov -ar 16000 -ac 1 -c:a pcm_s16le audio.wav`
4. `whisper-cli -m models\ggml-large-v3-turbo.bin -f audio.wav -l ar -ml 1 -ojf -of audio`
   (`-l de` für Deutsch, `-ml 1` = ein Wort pro Segment, `-ojf` = JSON mit Zeitstempeln).
5. `audio.json` zurück ins Projekt, daraus die Wortliste bauen.

### Qualität
- Ägyptischer Dialekt wird nicht perfekt erkannt: immer mit Skripttext gegenlesen, Zahlen und Fachwörter (ETF, Trade Republic) prüfen.
- Zeitstempel auf ±40 ms prüfen: Untertitel kommen 0,08 s vor dem Wort.

## 08 B-Roll: passende Zwischenbilder

### Quellen (alle kostenlos)
1. Karims eigene B-Roll (am besten): Laptop, Kaffee, Berliner Straße, Unterschrift, Handy mit Depot (Zahlen unkenntlich). Einmal 20 Clips à 3 s drehen lassen, Ordner `broll/` im Projekt.
2. Coded B-Roll mit der Frame-Engine (Charts, Zinseszins-Kurve, Icons).
3. Stock: Pexels API (`https://api.pexels.com/videos/search?query=…&orientation=portrait`, Header `Authorization: <key>`) und Pixabay API. Beide brauchen einen kostenlosen Schlüssel; Karim legt ihn als Umgebungs-Secret an, nie ins Gedächtnis oder in Dateien schreiben. Netzwerk vorher kurz testen.

### Lizenz
Pexels/Pixabay: kommerziell frei, keine Namensnennung nötig. Aber: keine erkennbaren Marken/Logos, keine Personen so zeigen, als würden sie Karim empfehlen.

### Einsatz
- 1 bis 2 s pro Clip, genau auf dem Wort, das es zeigt.
- Höchstens ein Drittel des Talking-Videos B-Roll; Karims Gesicht trägt das Vertrauen.
- Farbe an den Look angleichen (02).
- Bei Yalla-Videos: Bilder, mit denen sich Ägypter in Deutschland identifizieren, nichts Klischeehaftes.

## 09 Export und Safe Zones

### Hauptdatei (Reel/TikTok/FB/Story)
- 1080×1920, Quell-fps beibehalten (meist 30), H.264 High, yuv420p, `-movflags +faststart`.
- Instagram: crf 22, `-maxrate 2450k -bufsize 4900k`, Datei < 25 MB (Karims Vorgabe). TikTok/FB dürfen gleich bleiben.
- Audio AAC 48 kHz, 192 kbit/s.

### Safe Zones
Overlay `/mnt/project-files/skills/video/assets/safe_zones_9x16.png` über einen Prüf-Frame legen (`overlay`). Ungefähr:
- oben 220 px frei (Kontoname, Tabs), unten 480 px frei (Caption, Musik), rechts 140 px ab Bildmitte abwärts (Buttons).
- Untertitel also zwischen etwa y=1150 und y=1440, unter dem Kinn, nie im roten Bereich. Karims Regel: die unteren 25 % (ab y=1440) bleiben immer frei.
- Werte sind Näherungen; wenn eine Plattform ihr Layout ändert, Overlay hier anpassen.

### Weitere Fassungen
- Feed 4:5 (1080×1350): auf Gesicht zentriert zuschneiden, Texte neu setzen statt abschneiden.
- Titelbild 1080×1920: Headline groß, Karim klein (Karims Vorgabe), Inhalt in der grünen 3:4-Fläche (Profil-Raster).
- Gleiches Video nicht doppelt auf einem Konto; für TikTok kein Instagram-Wasserzeichen.

### Benennung
`<datum>_<marke>_<thema>_v<n>.mp4` und daneben `caption.txt` (Caption, Hashtags über `hashtags-finden`).

## 10 QA vor dem Upload

Nichts geht an Karim, bevor alles hier grün ist. Ergebnis als kurze Liste mitschicken.

### Technik (automatisch)
- `ffprobe`: 1080×1920, fps, Dauer, Größe < 25 MB (IG).
- Lautheit: `ffmpeg -i out.mp4 -af loudnorm=print_format=json -f null -` → -14 ±1 LUFS, TP ≤ -1 dBTP.
- `blackdetect=d=0.1`, `freezedetect=n=0.003:d=0.5` (außer gewollte Standbilder), `silencedetect=n=-45dB:d=0.6` (lange Löcher im Ton).
- A/V-Sync: Ausgabe-Ton gegen Sprachspur an 3 Stellen kreuzkorrelieren, Abweichung konstant und < 40 ms.

### Bild (ansehen)
- Kontaktbogen: `ffmpeg -i out.mp4 -vf "fps=2,scale=216:-1,tile=8x6" -frames:v 1 sheet.jpg`, plus Einzelbilder an jedem Grafik-Einstieg.
- Frame 1 zeigt den Hook. Nichts auf Gesicht/Kopf. Untertitel nie zwei Zeilen übereinander, kommen 0,08 s vor dem Wort.
- Safe-Zone-Overlay (09) auf 3 Frames. Loop-Naht: letzter und erster Frame nebeneinander.
- Arabisch: von rechts nach links, Buchstaben verbunden, Zahlen richtig herum.

### Inhalt
- Rechtschreibung DE/AR/EN in allen Texten im Bild und in der Caption.
- `werberecht-finanzberater`: kein "unabhängig" ohne Honorarberatung, keine Garantien, Risikohinweis wenn nötig.
- CTA-Wort im Video und in der Caption identisch.

---
# Anhang B: Start-Register
## Video-Register: alles, was die Video-Regie einbindet

Jeder neue Skill, jedes neue Tool oder jede neue Vorlage, die bei Videos helfen kann, kommt hier als eine Zeile rein
(egal in welchem Thread sie entsteht). Format: `Name | wofür | wann einsetzen | Pfad oder Skill-Name | Datum`.

### Formate (eins davon trägt das Video)
- loft-explainer | animierte Erklärvideos über Voiceover ("3 Geldfehler" v1) | jedes Erklär-/Loft-Video | Skill | 20.10.2026
- yalla-reel-editor | Talking-Reels @yallafinanzen (Steuer-Reel v3, Arabisch RTL) | Standard für Talking-Videos AR | Skill | 17.10.2026
- green-dynamic | alternativer Talking-Look | nur wenn Karim "green dynamic" sagt | Skill | 20.10.2026
- Autoschnitt | deutsche Talking-Videos (Der Finanzhausarzt) | Talking-Videos DE | /mnt/project-files/knowledge/autoschnitt/ | vor 16.10.2026

### Motor und Bausteine für Grafik
- frame-engine | Code malt jeden Frame, echte Federn, Sound im Code | jede animierte Grafik | Skill | 20.10.2026
- web-video-toolkit | HyperFrames (Übergänge, Caption-Styles, SFX) + Remotion | zum Ergänzen, nie statt der Formate | Skill | 25.10.2026
- remotion-best-practices | Remotion-Regeln | wenn Remotion genutzt wird | Skill | 25.10.2026

### Die 10 Profi-Bausteine (30.10.2026)
- 01 Ton-Studio | bausteine/01_ton-studio.md | jedes Video mit Stimme
- 02 Farb-Look | bausteine/02_farb-look.md + assets/karim_warm.cube | jedes gefilmte Video
- 03 Freistellen | bausteine/03_freistellen.md | Karten hinter Karim, Split-Screen
- 04 Retention-Schnitt | bausteine/04_retention-schnitt.md | jedes Video
- 05 Dreh-Check | bausteine/05_dreh-check.md | bei Testbild/Probe oder schwacher Aufnahme
- 06 Skript & Teleprompter | bausteine/06_skript-teleprompter.md | wenn noch kein Skript da ist
- 07 Transkription | bausteine/07_transkription-lokal.md | jedes Video (Untertitel, Schnitt)
- 08 B-Roll | bausteine/08_b-roll.md | Talking-Videos mit Platz für Zwischenbilder
- 09 Export & Safe Zones | bausteine/09_export-safe-zones.md + assets/safe_zones_9x16.png | jedes Video
- 10 QA vor Upload | bausteine/10_qa-vor-upload.md | jedes Video, immer zuletzt

### Texte rund ums Video
- hooks-captions-offers | Hook, Bildschirmtext, Caption, CTA | jedes Video | Skill
- werberecht-finanzberater | rechtliche Prüfung | jedes Video | Skill
- text-humanisieren / texte-schreiben | keine KI-Floskeln | Skript und Caption | Skill
- hashtags-finden | 3 bis 5 Hashtags | Caption | Skill
- content-planung | Thema und Wiederverwertung | wenn Thema offen ist | Skill
- canvas-design | Titelbilder | Reel-Titelbild | Skill

### Neu hinzugekommen
(hier neue Zeilen anhängen)

---
# Anhang C: Assets erzeugen
Nach `assets/` im Arbeitsordner ausführen (python3 mit numpy und Pillow):
```python
import numpy as np
from PIL import Image, ImageDraw, ImageFont
N=33; g=np.linspace(0,1,N); L=['TITLE "karim_warm"','LUT_3D_SIZE 33']
for b in g:
  for gg in g:
    for r in g:
      c=np.clip(0.5+(np.array([r,gg,b])-0.5)*1.06,0,1); c=c+0.04*np.sin(np.pi*c)*(c-0.5)
      y=0.2126*c[0]+0.7152*c[1]+0.0722*c[2]
      sat=1.03 if (r>gg>b and r-b>0.06) else 1.08
      c=y+(c-y)*sat
      c=c+np.array([0.012,0.004,-0.012])*(1-abs(y-0.5)*1.2)
      c=c+np.array([-0.006,0,0.008])*max(0,0.35-y)/0.35
      L.append('%.5f %.5f %.5f'%tuple(np.clip(c,0,1)))
open('karim_warm.cube','w').write('\n'.join(L)+'\n')
im=Image.new('RGBA',(1080,1920),(0,0,0,0)); d=ImageDraw.Draw(im); red=(214,69,69,110)
d.rectangle([0,0,1080,220],fill=red); d.rectangle([0,1440,1080,1920],fill=red)
d.rectangle([940,700,1080,1440],fill=red)
d.rectangle([0,240,1080,1680],outline=(30,160,90,220),width=6)
im.save('safe_zones_9x16.png')
```