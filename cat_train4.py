import cv2

face_cascade = cv2.CascadeClassifier("C:\\Users\\user\\Desktop\\CS\\practice\\opencv\\cat.xml")

img = cv2.imread("C:\\Users\\user\\Desktop\\CS\\practice\\opencv\\cat1.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3,
                                      minNeighbors=10, minSize=(75, 75))

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0,0,255), 3)
    cv2.rectangle(img, (x, y - 40), (x + w, y), (0,0,255), -1)
    cv2.putText(img, "Cat", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
