# -*- coding: utf-8 -*-
"""task 2-1 (1) .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VzJNGoJFTXGTGDBTvvQXeY2NaYuwqYn2
"""

# Commented out IPython magic to ensure Python compatibility.
import cv2
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
from google.colab.patches import cv2_imshow
print('Imported')

blank_img=np.zeros((512,512,3),dtype=np.int16)
blank_img.shape

plt.imshow(blank_img)

cv2.rectangle(blank_img,pt1=(350,0),pt2=(510,150),color=(0,255,0),thickness=5)

plt.imshow(blank_img)

cv2.rectangle(blank_img,pt1=(200,200),pt2=(300,300),color=(255,0,0),thickness=5)

plt.imshow(blank_img)

cv2.circle(img=blank_img,center=(100,100),radius=50,color=(0,0,255),thickness=8)
plt.imshow(blank_img)

cv2.line(blank_img,pt1=(0,0),pt2=(512,512),color=(92,255,255),thickness=4)
plt.imshow(blank_img)

font = cv2.FONT_ITALIC
cv2.putText(blank_img,text='Hello',org=(10,500),fontFace=font,fontScale=4,color=(255,255,255),thickness=4,lineType=cv2.LINE_AA)
plt.imshow(blank_img)