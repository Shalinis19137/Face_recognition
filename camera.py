import cv2
cam = cv2.VideoCapture(0)
cv2.namedWindow("Screenshot")
img_counter=0
while(True):
    ret,frame = cam.read()
    if not ret:
        print("Failed to grab")
        break
    cv2.imshow("Test",frame)
    k  = cv2.waitKey(2)
    if(k == ord("a")):
        print("Closing ")
        break
    elif(k == ord("c")):
        img_name ="C:/Users/lorem/Desktop/face recognitation system".format(img_counter)
        cv2.imwrite(img_name,frame)
        print("SC taken")
        img_counter+=1
cam.release()
cam.destroyAllWindows()