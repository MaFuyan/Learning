import os
import glob
import Image
import cv2

image_dir = "/home/chen/Pictures/dataset/icdar/icdar2017rctw_train_v1.2/gt_line_result/*.jpg"
imgDirs = []
imgLists = glob.glob(image_dir)

imgs_save_dir = "/home/chen/Pictures/dataset/icdar/icdar2017rctw_train_v1.2/gt_line_500/"

for item in imgLists:
	imgDirs.append(item)

for img_dir in imgDirs:
    img = cv2.imread(img_dir)
    img_basename = os.path.basename(img_dir)
    res=cv2.resize(img,(500,500))
    cv2.imwrite(os.path.join(imgs_save_dir,img_basename),res)
