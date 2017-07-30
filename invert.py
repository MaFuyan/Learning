import os
import glob
import Image
import cv2

image_dir = "/home/csb/Downloads/dataset/icdar2017rctw_train_v1.2/gt_gray/*.png"
imgDirs = []
imgLists = glob.glob(image_dir)

imgs_save_dir = "/home/csb/Downloads/dataset/icdar2017rctw_train_v1.2/gt_image/"

for item in imgLists:
	imgDirs.append(item)

for img_dir in imgDirs:
    img = cv2.imread(img_dir,0)
    img_basename = os.path.basename(img_dir)
    ret,thresh=cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
    cv2.imwrite(os.path.join(imgs_save_dir,img_basename),thresh)