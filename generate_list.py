import os
import glob

f = open('test_new.lst','w')
for i in range(1,4229):
	print >>f,'train_all/train_01/image_'+str(i)+'.jpg'+" "+"gt_test/image_"+str(i)+".png"
f = open('train.lst','a+')
for i in range(1001,2001):
	print >>f,'train_all/train_02/image_'+str(i)+'.jpg'+" "+"gt_all/gt_02/image_"+str(i)+".jpg" 
f = open('train.lst','a+')
for i in range(2001,3001):
	print >>f,'train_all/train_03/image_'+str(i)+'.jpg'+" "+"gt_all/gt_03/image_"+str(i)+".jpg" 
f = open('train.lst','a+')
for i in range(3001,4001):
	print >>f,'train_all/train_04/image_'+str(i)+'.jpg'+" "+"gt_all/gt_04/image_"+str(i)+".jpg" 
f = open('train.lst','a+')
for i in range(4001,5001):
	print >>f,'train_all/train_05/image_'+str(i)+'.jpg'+" "+"gt_all/gt_05/image_"+str(i)+".jpg" 
f = open('train.lst','a+')
for i in range(5001,6001):
	print >>f,'train_all/train_06/image_'+str(i)+'.jpg'+" "+"gt_all/gt_06/image_"+str(i)+".jpg" 
f = open('train.lst','a+')
for i in range(6001,7001):
	print >>f,'train_all/train_07/image_'+str(i)+'.jpg'+" "+"gt_all/gt_07/image_"+str(i)+".jpg" 
for i in range(7001,8034):
	print >>f,'train_all/train_08/image_'+str(i)+'.jpg'+" "+"gt_all/gt_08/image_"+str(i)+".jpg" 

