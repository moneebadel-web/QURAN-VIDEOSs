# 09 Export und Safe Zones

## Hauptdatei (Reel/TikTok/FB/Story)
- 1080×1920, Quell-fps beibehalten (meist 30), H.264 High, yuv420p, `-movflags +faststart`.
- Instagram: crf 22, `-maxrate 2450k -bufsize 4900k`, Datei < 25 MB (Karims Vorgabe). TikTok/FB dürfen gleich bleiben.
- Audio AAC 48 kHz, 192 kbit/s.

## Safe Zones
Overlay `/mnt/project-files/skills/video/assets/safe_zones_9x16.png` über einen Prüf-Frame legen (`overlay`). Ungefähr:
- oben 220 px frei (Kontoname, Tabs), unten 480 px frei (Caption, Musik), rechts 140 px ab Bildmitte abwärts (Buttons).
- Untertitel also zwischen etwa y=1150 und y=1440, unter dem Kinn, nie im roten Bereich.
- Werte sind Näherungen; wenn eine Plattform ihr Layout ändert, Overlay hier anpassen.

## Weitere Fassungen
- Feed 4:5 (1080×1350): auf Gesicht zentriert zuschneiden, Texte neu setzen statt abschneiden.
- Titelbild 1080×1920: Headline groß, Karim klein (Karims Vorgabe), Inhalt in der grünen 3:4-Fläche (Profil-Raster).
- Gleiches Video nicht doppelt auf einem Konto; für TikTok kein Instagram-Wasserzeichen.

## Benennung
`<datum>_<marke>_<thema>_v<n>.mp4` und daneben `caption.txt` (Caption, Hashtags über `hashtags-finden`).
