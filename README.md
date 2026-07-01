# simple_face_detection_and_counting
this is the first python code i write ever ::
#explaining&how to use:
firstly this code is using a library called open_cv 
you can install using terminal:
```bash
pip install opencv-python

#then download haar_cascade  but what is this:
asfa its like pre trained model that is trained on how to detect something its like an algorithm that can  and we can call it classier model 

#python code explained:
import cv2-> this says we will be  using cv library so  get it 
img=cv2.imread('img path here')->we firstly read the image in a way  machine can understand using this function
classified_img=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')-> this function start using  haar_cascade to( it detects faces in it after we read  using haar-cascade classifier we used)
posistions=classified_img.detectMultiScale(img)->this returns positions  of faces to place rectangles later it return is a list of lists or (matrix)  looks like this:
<img width="438" height="203" alt="لقطة شاشة 2026-07-02 014732" src="https://github.com/user-attachments/assets/b32f1e15-a8d7-4c92-b5a7-7a860fcef1fc" />
  first  is the first value of x in point 1(start) in width(x)
second is the first value of y in point 1(start) in height(y)
then the third is the width of the face and 4th is the height 
then lets connect them in a rectangle for each face:
for(x,y,w,h) in posistions:
    cv2.rectangle(img,(x,y),(x+w,w+h),(88,123,8),5)
    i=i+1
cv2.imshow('Face Detection',img)
cv2.waitKey(0)
print(i,'faces detected')

imshow to show img
waitkey ->means wait until  any key  is pressed









so to  get  each list that represents each face position




