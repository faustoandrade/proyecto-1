
# coding: utf-8

# In[15]:

import cv2

img = cv2.imread("chicas.jpg")
face_csc = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_csc.detectMultiScale(gray, 1.3, 2)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,0), 5)
    
cv2.imshow('chicas aguila', img)
cv2.waitKey(0)


# In[ ]:



