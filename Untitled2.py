#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('python -m pip install easyocr')


# In[15]:


import os
import warnings
import easyocr  

os.environ['CUDA_VISIBLE_DEVICES'] = ''  
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  
warnings.filterwarnings("ignore")  

# Create the reader instance
language_list = ['en']  # Local variable: list of languages
reader = easyocr.Reader(language_list, gpu=False)  # Instance: EasyOCR reader object
image_path = 'C:/Users/VARSHITHA V/Pictures/Screenshots/Screenshot 2025-04-26 200434.png'  # Path to your image
results = reader.readtext(image_path)  # Local variable: list of (bbox, text, confidence)
for result in results:
    bbox, text, confidence = result  # Local variables: bounding box, text, probability
    print(f"Detected: '{text}' with confidence {confidence:.2f}")


# In[7]:


get_ipython().system('python -m pip install opencv-python')


# In[12]:


import os
import warnings
import cv2
import easyocr
import matplotlib.pyplot as plt
os.environ['CUDA_VISIBLE_DEVICES'] = ''
warnings.filterwarnings("ignore")
reader = easyocr.Reader(['en'], gpu=False)
image_path = 'C:/Users/VARSHITHA V/Pictures/Screenshots/Screenshot 2025-04-26 200434.png'
image = cv2.imread(image_path)
results = reader.readtext(image_path)
for bbox, text, prob in results:
    (top_left, top_right, bottom_right, bottom_left) = bbox
    top_left = tuple(map(int, top_left))
    bottom_right = tuple(map(int, bottom_right))

    cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)
    cv2.putText(image, text, (top_left[0], top_left[1] - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.figure(figsize=(12, 8))
plt.imshow(image_rgb)
plt.axis('off')
plt.title("OCR Result")
plt.show()


# In[ ]:




