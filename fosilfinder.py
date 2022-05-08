import streamlit as st
import cv2
import numpy as np
from PIL import Image

while(True):
    url = "http://10.216.4.182:8080/shot.jpg"
    cp = cv2.VideoCapture(url)
    camera, frame = cp.read()
    if frame is not None:
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        im_pil = Image.fromarray(img)
        
        #cv2.imshow("Frame", frame) # mostrar tipo cv2
        st.image(im_pil, caption='Sunrise by the mountains')

    #q = cv2.waitKey(1)
    #if q==ord("q"):
        #break
    
    #cv2.destroyAllWindows()
