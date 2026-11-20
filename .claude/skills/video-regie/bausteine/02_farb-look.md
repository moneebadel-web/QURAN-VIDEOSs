# 02 Farb-Look: jedes Video gleich hochwertig

Ziel: gleicher Hautton und Look in allen Videos, egal ob Fenster- oder Lampenlicht.

## 1. HDR erkennen und auf SDR bringen
`ffprobe -v error -select_streams v:0 -show_entries stream=color_transfer,color_primaries -of csv=p=0 in.mov`
- `arib-std-b67` (HLG) oder `smpte2084` (PQ) = iPhone-HDR. Dann:
  `zscale=t=linear:npl=100,format=gbrpf32le,zscale=p=bt709,tonemap=hable:desat=0,zscale=t=bt709:m=bt709:r=tv,format=yuv420p`
- Danach Hautton prüfen: hable macht oft etwas flach, darum folgt Schritt 2.

## 2. Korrektur (pro Video, messen statt raten)
- Gesichtsbereich messen (MediaPipe face_landmarker oder Mitte oberes Drittel): Ziel-Luma Gesicht ≈ 0.55 bis 0.65, Rot > Grün > Blau, R−B ≈ 0.10 bis 0.18.
- Zu kühl: `colorbalance=rm=0.04:bm=-0.04`. Zu dunkel: `eq=gamma=1.08` (nicht brightness, das hebt Schwarz an).
- Grünstich (Leuchtstofflampe): `colorbalance=gm=-0.03`.

## 3. Look
`lut3d=/mnt/project-files/skills/video/assets/karim_warm.cube` (warm in den Mitten, leicht kühle Schatten, Hauttöne geschützt).
Stärke regeln: Look-Ebene mit `blend=all_mode=normal:all_opacity=0.7` über die korrigierte Ebene.
Look nur ändern, wenn Karim es sagt. Neue Looks als eigene .cube in `assets/` ablegen und hier eintragen.

## 4. Kontrolle
Ein Standbild vorher/nachher nebeneinander (`hstack`) ansehen: Haut natürlich, keine orangene Stirn, Weiß bleibt weiß.
