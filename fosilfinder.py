import streamlit as st
import cv2
import numpy as np
from PIL import Image
import ftplib


session = ftplib.FTP('ftp.inmobiliariaune.com','ftp.inmobiliariaune.com','BDoM3xtL')

url = "http://10.216.4.182:8080/shot.jpg"
cp = cv2.VideoCapture(url)
camera, frame = cp.read()
img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
im_pil = Image.fromarray(img)
im_pil.save("fosil", 'PNG') # fn is a filename
file = open('fosil','rb')                  # file to send
session.storbinary('STOR /public/fosil/fosil.jpg', file)     # send the file
#file.close()                                    # close file and FTP
session.quit()
#cv2.imshow("Frame", file) # mostrar tipo cv2
#cv2.destroyAllWindows()

#while(True):
    #url = "http://10.216.4.182:8080/shot.jpg"
   # cp = cv2.VideoCapture(url)
   # camera, frame = cp.read()
   # if frame is not None:
   #     img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
  #      im_pil = Image.fromarray(img)
   #     
        #cv2.imshow("Frame", frame) # mostrar tipo cv2
   #     st.image(im_pil, caption='Sunrise by the mountains')
#//////
    #q = cv2.waitKey(1)
    #if q==ord("q"):
        #break
    #//////

    #cv2.destroyAllWindows()
