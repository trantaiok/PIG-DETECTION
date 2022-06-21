import cv2
path =  "D:/NHAN_DIEN_HEO/NHANDIENHEO/image_th/"
for i in range(0, 20):  
    print(path+str(i)+'.jpg') 
    img = cv2.imread(path +str(i)+'.jpg') 
    img5050 = cv2.resize(img, (100,100))
    cv2.imshow("img",img5050)
    cv2.waitKey(20)
    cv2.imwrite('D:/NHAN_DIEN_HEO/NHANDIENHEO/image_th/'+'heo'+str(i+1000)+'.jpg', img5050)