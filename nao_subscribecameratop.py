import cv2

counter = 0

while True:

    if counter == 100:

        try:
            img = cv2.imread('nao_cameratop.jpg')
            img_bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
            cv2.imshow('Camera NAO Top', img_bgr)
            cv2.waitKey(1)
            counter = 0
        except:
            pass
    else:
        counter +=1
        #print(counter)    

cv2.destroyAllWindows()

