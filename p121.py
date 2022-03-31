from tkinter import Frame
import cv2
import time
import numpy as np

fourcc=cv2.VideoWriter_fourcc(*"XVID")
outputfile=cv2.VideoWriter("Output.avi1" , fourcc , 20.0 , (640,480))
cap=cv2.VideoCapture(0)

time.sleep(2)

bg=0

for i in range (60) :
    ret,bg=cap.read()
bg=np.flip(bg , axis=1)

while cap.isOpened():
    ret,img=cap.read()
    if not ret:
        break
    img=np.flip(img , axis=1)

    hsv=cv2.cvtColor(img , cv2.COLOR_BGR2HSV)
    
    l_black = np.array([30,30,0]) 
    u_black = np.array([104,153,70]) 
    mask_1 = cv2.inRange(hsv, l_black, u_black) 
    
    
    mask_1 =cv2.morphologyEx(mask_1 , cv2.MORPH_OPEN , np.ones((3,3) , np.uint8))
    mask_1 =cv2.morphologyEx(mask_1 , cv2.MORPH_DILATE , np.ones((3,3) , np.uint8))

    res_2=cv2.bitwise_and(bg , bg , mask=mask_1)

    final_output=cv2.addWeighted(res_2 , 1 , res_2 , 1 , 0)
    outputfile.write(final_output)
    cv2.imshow("Magic" , final_output)
    #cv2.waitKey(1)
    
    if cv2.waitKey(5)==ord("q"):
        break
    
cap.release()
outputfile.release()
cv2.destroyAllWindows()    
