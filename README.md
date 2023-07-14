# USB-Kamera-Gesichtserkennung

Dieses Projekt zeigt, wie man mithilfe einer USB-Kamera und OpenCV die Gesichtserkennung durchführt und überprüft, ob ein bestimmtes Gesicht (z.B. das eines Kollegen) erkannt wird.

## Voraussetzungen

Um dieses Programm auszuführen, benötigen Sie:

- Eine USB-Kamera, die an Ihren Computer angeschlossen ist.
- Python 3 und OpenCV müssen auf Ihrem System installiert sein.

## Anleitung

1. Klonen Sie dieses Repository auf Ihren Computer:

```
git clone https://github.com/your-username/usb-kamera-gesichtserkennung.git
```


2. Navigieren Sie in das Projektverzeichnis:

```
cd usb-kamera-gesichtserkennung
```


3. Installieren Sie die erforderlichen Python-Pakete. Es wird empfohlen, ein virtuelles Python-Umfeld zu verwenden:

```
python3 -m venv venv
```
```
source venv/bin/activate (Linux/Mac)
```
```
venv\Scripts\activate (Windows)
```
```
pip install -r requirements.txt
```

4. Laden Sie das vorher trainierte Gesichtserkennungsmodell herunter. Sie können das Modell "haarcascade_frontalface_default.xml" von der OpenCV-Website herunterladen und im Projektverzeichnis speichern.

5. Laden Sie das Bild des Kollegen herunter und speichern Sie es im Projektverzeichnis. Stellen Sie sicher, dass das Bild im JPEG-Format vorliegt.

6. Führen Sie das Programm aus:
```
python main.py
```

7. Die Kamera öffnet sich, und das Programm versucht, das Gesicht des Kollegen in Echtzeit zu erkennen. Wenn das Gesicht des Kollegen erkannt wird, wird ein grünes Rechteck um das Gesicht gezeichnet und die Nachricht "Kollege erkannt!" wird darüber angezeigt.

8. Beenden Sie das Programm, indem Sie die Taste "q" drücken.

## Anpassungen

- Sie können die Parameter `scaleFactor` und `minNeighbors` in der Datei `main.py` anpassen, um die Genauigkeit der Gesichtserkennung zu beeinflussen. Experimentieren Sie mit verschiedenen Werten, um die besten Ergebnisse zu erzielen.

- Wenn Sie ein anderes Bild des Kollegen verwenden möchten, ersetzen Sie das vorhandene Bild "colleague.jpg" im Projektverzeichnis durch das gewünschte Bild. Achten Sie darauf, dass das Bild im JPEG-Format vorliegt.

- Wenn Sie ein anderes Gesichtserkennungsmodell verwenden möchten, können Sie es herunterladen und im Projektverzeichnis speichern. Aktualisieren Sie dann den Pfad zum Modell in der Datei `main.py`.
