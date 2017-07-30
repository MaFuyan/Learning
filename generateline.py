import os
import glob
import Image, ImageDraw

# ground truth directory
gt_text_dir = "/home/chen/Pictures/dataset/icdar/icdar2017rctw_train_v1.2/data/train_gt_text"

# original images directory
image_dir = "/home/chen/Pictures/dataset/icdar/icdar2017rctw_train_v1.2/data/train_gt_blank/*.jpg"
imgDirs = []
imgLists = glob.glob(image_dir)

# where to save the images with ground truth boxes
imgs_save_dir = "/home/chen/Pictures/dataset/icdar/icdar2017rctw_train_v1.2/data/gt_line_500"

for item in imgLists:
    imgDirs.append(item)

for img_dir in imgDirs:
    img = Image.open(img_dir)
    dr = ImageDraw.Draw(img)    

    img_basename = os.path.basename(img_dir)
    (img_name, temp2) = os.path.splitext(img_basename)
    # open the ground truth text file
    img_gt_text_name = img_name + ".txt"
    print img_gt_text_name

    bf = open(os.path.join(gt_text_dir, img_gt_text_name)).read().decode("utf-8-sig").encode("utf-8").splitlines()

    for idx in bf:
        rect = []
        spt = idx.split(',')
        a = float(spt[2])-float(spt[0])+float(spt[1])-float(spt[3])
        b = float(spt[4])-float(spt[2])+float(spt[5])-float(spt[3])
        if a>b:
            rect.append(float(spt[0])*0.75+float(spt[6])*0.25)
            rect.append(float(spt[1])*0.75+float(spt[7])*0.25)
            rect.append(float(spt[2])*0.75+float(spt[4])*0.25)
            rect.append(float(spt[3])*0.75+float(spt[5])*0.25)
            rect.append(float(spt[2])*0.25+float(spt[4])*0.75)
            rect.append(float(spt[3])*0.25+float(spt[5])*0.75)
            rect.append(float(spt[0])*0.25+float(spt[6])*0.75)
            rect.append(float(spt[1])*0.25+float(spt[7])*0.75)
        else:
            rect.append(float(spt[0])*0.75+float(spt[2])*0.25)
            rect.append(float(spt[1])*0.75+float(spt[3])*0.25)
            rect.append(float(spt[2])*0.75+float(spt[0])*0.25)
            rect.append(float(spt[3])*0.75+float(spt[1])*0.25)
            rect.append(float(spt[6])*0.25+float(spt[4])*0.75)
            rect.append(float(spt[7])*0.25+float(spt[5])*0.75)
            rect.append(float(spt[4])*0.25+float(spt[6])*0.75)
            rect.append(float(spt[5])*0.25+float(spt[7])*0.75)
        dr.polygon((rect[0], rect[1], rect[2], rect[3], rect[4], rect[5], rect[6], rect[7]), outline="white")

        # if a>b:
        #     offset = float(rect[5])-float(rect[3])
        # else:
        #     offset = float(rect[2])-float(rect[0])
        # for i in range(0,int(offset/2)+2):
        #     dr.polygon((rect[0]+i, rect[1]+i, rect[2]-i, rect[3]+i, rect[4]-i, rect[5]-i, rect[6]+i, rect[7]-i), outline="white")

#        rect.append(float(min(float(spt[0]),float(spt[6]))))
#      	 rect.append(float(min(float(spt[1]),float(spt[3]))))
#        rect.append(float(max(float(spt[2]),float(spt[4]))))
#        rect.append(float(min(float(spt[1]),float(spt[3]))))
#     	 rect.append(float(max(float(spt[2]),float(spt[4]))))
#        rect.append(float(max(float(spt[5]),float(spt[7]))))
#        rect.append(float(min(float(spt[0]),float(spt[6]))))
#        rect.append(float(max(float(spt[5]),float(spt[7]))))

        # # draw the polygon with (x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4)
        # for i,j in zip(range(0,int(rect[2]-rect[0])/2),range(0,int(rect[5]-rect[3])/2)):
        #     dr.polygon((rect[0]+i, rect[1]+j, rect[2]-i, rect[3]+j, rect[4]-i, rect[5]-j, rect[6]+i, rect[7]-j), outline="white")

    img.save(os.path.join(imgs_save_dir, img_basename))
