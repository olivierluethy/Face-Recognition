import cv2

# Laden des vorher trainierten Gesichtserkennungsmodells
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read('trained_model.yml')

# Laden des Bildes des Kollegen
colleague_img = cv2.imread('colleague.jpg')
gray_colleague_img = cv2.cvtColor(colleague_img, cv2.COLOR_BGR2GRAY)

# Erkennen des Gesichts im Bild des Kollegen
faces = face_cascade.detectMultiScale(gray_colleague_img, scaleFactor=1.1, minNeighbors=5)
(x, y, w, h) = faces[0]
colleague_face = gray_colleague_img[y:y+h, x:x+w]

# Öffnen der Kamera
cap = cv2.VideoCapture(0)

while True:
    # Lesen eines Bildes von der Kamera
    ret, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Erkennen von Gesichtern im Kamerabild
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        # Extrahieren des erkannten Gesichts
        face = gray_frame[y:y+h, x:x+w]

        # Vergleichen des erkannten Gesichts mit dem Bild des Kollegen
        label, confidence = face_recognizer.predict(face)
        if label == 0:
            # Wenn das erkannte Gesicht dem Bild des Kollegen entspricht
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, 'Kollege erkannt!', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
            # Hier könnte der Code eingefügt werden, um die Tür zu öffnen

    # Anzeigen des Kamerabildes
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
