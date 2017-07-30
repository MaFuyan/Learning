import os
import glob

f = open('train_line.lst','w')
for i in range(0,8034):
	print >>f,'train_500/image_'+str(i)+'.jpg'+" "+"gt_line_500/image_"+str(i)+".jpg"
