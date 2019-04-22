
# coding: utf-8

# In[21]:


'''
!pip3 install pytesseract
!sudo apt install tesseract-ocr
!sudo apt install libtesseract-dev
'''

import pytesseract
from PIL import Image

def read_image(img):
    text=pytesseract.image_to_string(image)
    return text

def read_image_path(path):
    image=Image.open(path)
    text=pytesseract.image_to_string(image)
    return text



# In[ ]:



#Oneliner
#print(pytesseract.image_to_string(Image.open('image.jpg')))

