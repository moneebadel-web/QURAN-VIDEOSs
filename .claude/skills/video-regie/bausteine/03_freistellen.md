# 03 Freistellen: Person sauber vom Hintergrund

Gebraucht für: Karten/Text hinter Karim, Split-Screen mit Kopf-Pop-out, Hintergrund abdunkeln.

## Weg A (Container): MediaPipe
- Modell `selfie_multiclass.tflite` aus `/mnt/project-files/reels/pipeline/models/` und `matte.py` aus `edit/`.
- Alpha = clip((0.75−bg)/0.4), danach Kanten: 2× Erosion, dann 3 px Weichzeichnen.
- Gegen Flackern: Alpha zeitlich glätten (EMA, 0.6 aktuell + 0.4 vorher), bei schnellen Bewegungen weniger glätten.
- Matte nach jeder Schnittänderung neu berechnen.

## Weg B (bessere Haare, läuft auf Karims Laptop): RobustVideoMatting
- Kostenlos (GPL-3.0, eigene Nutzung ok). ONNX-Modell `rvm_mobilenetv3_fp32.onnx` aus den GitHub-Releases von PeterL1n/RobustVideoMatting, Python mit onnxruntime.
- Im Container ist PyPI gesperrt, daher per Remote-Control-Sitzung auf dem Laptop ausführen und nur das Alpha-Video (ProRes 4444 oder PNG-Folge) zurückholen.

## Regeln
- Nie Text über Gesicht oder Kopf (Karims Regel).
- Vor dem Planen an 3 s testen: Kanten an Haaren und Händen ansehen (Kontaktbogen).
- Ohne gute Matte lieber Layout ohne Freistellen wählen als Kanten zeigen.
