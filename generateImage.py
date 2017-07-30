import os
import glob
import Image

image_dir = "/home/csb/Downloads/dataset/icdar2017rctw_train_v1.2/train_image/*.jpg"
imgDirs = []
imgLists = glob.glob(image_dir)

imgs_save_dir = "/home/csb/Downloads/dataset/icdar2017rctw_train_v1.2/train_gt_blank"

for item in imgLists:
	imgDirs.append(item)

for img_dir in imgDirs:
    img = Image.open(img_dir)
    width,height = img.size

    img_basename = os.path.basename(img_dir)
    (img_name, temp2) = os.path.splitext(img_basename)
    Image.new("1",(width,height)).save(os.path.join(imgs_save_dir,img_basename))

