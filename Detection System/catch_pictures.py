import cv2

video_path = 'test100.mp4'

cap = cv2.VideoCapture(video_path)

ret, frame = cap.read()
i = 0

while ret:
    cv2.resize(frame, (606, 608))
    cv2.imwrite('pictures/{}.jpg'.format(str(i)), frame)
    ret, frame = cap.read()
    i = i + 1
