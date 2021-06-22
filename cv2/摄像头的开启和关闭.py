import cv2

vc = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cap=cv2.VideoWriter(*‘XVID') #录制视频
cap=cv2.imwrite('image2/' + str(c) + '.jpg', frame)  #截图
vc.release()
cap.release()
