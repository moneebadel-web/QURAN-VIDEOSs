# 01 Ton-Studio: Stimme wie im Studio

Ziel: klare, warme Stimme, kein Hall, kein Rauschen, -14 LUFS, Musik immer unter der Stimme.
Wenn `/mnt/project-files/reels/pipeline/` da ist: dessen Kette (dereverb.py, sh.rnnn, music7.py, qa7.py) hat Vorrang, sie ist von Karim abgenommen.

## Messen zuerst
- Rauschboden: 2 s Stille aus dem Rohvideo, `ffmpeg -i in.wav -af astats -f null -` (RMS level). Über -50 dB = laut, RNNoise mit mix 0.95; unter -60 dB = mix 0.5 reicht.
- Hall: Ausklingen nach Satzende anhören bzw. mit `revstat.py` messen. Hörbarer Hall: erst Dereverb (WPE), dann die Kette.

## Standardkette (Sprache)
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

## Musik und SFX
- Musik etwa 20 dB unter der Stimme, zusätzlich Ducking:
  `[musik][stimme]sidechaincompress=threshold=0.02:ratio=8:attack=20:release=300[m]`
- SFX (Whoosh, Pop, Klick) nur auf Bildwechsel und Zahlen, nie über ein Schlüsselwort. Quelle: synthetisierte SFX der Frame-Engine oder HyperFrames-SFX-Bibliothek (web-video-toolkit).
- Am Ende: `alimiter=limit=0.63:level=0:latency=1` (level immer 0). Ziel nach AAC: -14 ±1 LUFS, True Peak ≤ -1 dBTP.

## Prüfen
A/B-Schnipsel (roh vs. fertig, je 5 s) rendern und in QA (10) anhören bzw. messen.
