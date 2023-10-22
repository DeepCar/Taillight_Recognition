from imgaug import augmenters as iaa

import cv2

seq = iaa.BlendAlphaRegularGrid(nb_rows=(7, 4), nb_cols=(17, 17),foreground=iaa.Multiply(0.0))


imglist = []

img = cv2.imread('image.jpg')

imglist.append(img)

images_aug = seq.augment_images(imglist)

cv2.imwrite('new.jpg', images_aug[0])






