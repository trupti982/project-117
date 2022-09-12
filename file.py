import cv2 
#Read Image#  
iimg = cv2.imread("D:/coding/PRO-c116-Teacher-R
 # Display Colored Image #
 cv2.imshow("Trupti",img) 
 gray_img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY) 
 # Display Grayscale Image#
 cv2.imshow("Grayscale", gray_img) 
 print(gray_img)
  cv2.waitkey(0)


