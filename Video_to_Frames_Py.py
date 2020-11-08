from cv2 import cv2
 
# Opens the Video file
cap = cv2.VideoCapture(0)
i=0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    if i%10==0:
        cv2.imwrite('kang'+str(i)+'.jpg',frame)

    if cv2.waitKey(25) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break
    i+=1
 
cap.release()
cv2.destroyAllWindows()