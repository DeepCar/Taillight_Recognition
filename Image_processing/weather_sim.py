#Using os library to walk through folders
import os
import cv2
from skimage.filters import gaussian
from skimage import img_as_ubyte
from imagecorruptions import corrupt

img_number = 1
for root, dirs, files in os.walk("C:/Users/..../.../..."):
 for path,subdir,files in os.walk("."):
   for name in dirs:
       print (os.path.join(root, name)) # will print path of directories
   for name in files:
       print (os.path.join(root, name)) # will print path of files
       path = os.path.join(root, name)
       img= cv2.imread(path, 1)  #now, we can read each file since we have the full path
       #process each image - change color from BGR to RGB.
       from imagecorruptions import get_corruption_names

       for i in range(15):

               for severity in range(1):

                       corrupted = corrupt(img, corruption_number=i, severity=severity + 2)
                       cv2.imwrite(str(name)+"C"+str(i)+str('S5')+".jpg", corrupted)

       # corrupted = corrupt(img, corruption_number=12, severity=5)
       # cv2.imwrite(str(name), corrupted)