import cv2
cap = cv2.VideoCapture("car.mp4")
car = cv2.CascadeClassifier("car.xml")
while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cars = car.detectMultiScale(gray, 1.1, 3)
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)
    cv2.imshow("Cars", frame)
    if cv2.waitKey(1) == 27:
        break
cap.release()
