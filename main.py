import cv2
img=cv2.imread('faces.jpg.jpeg')
classified_img=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
posistions=classified_img.detectMultiScale(img)
i=0;
for(x,y,w,h) in posistions:
    cv2.rectangle(img,(x,y),(x+w,y+h),(88,23,8),1)
    i=i+1
cv2.imshow('Face Detection',img)
cv2.waitKey(0)
print(i,'faces detected')
