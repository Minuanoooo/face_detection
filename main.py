import cv2 as cv

face_cascade = cv.CascadeClassifier(
    cv.data.haarcascades + "haarcascade_frontalface_default.xml"
)

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret,frame = cap.read()

    if not  ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)
    for x, y, w, h in faces:
        print(x, y, w, h)
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        cv.putText(frame,'pidor', (x, y + h + 25), cv.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2, cv.LINE_AA)
    cv.imshow('frame',frame)
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()