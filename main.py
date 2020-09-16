#
# Put this module inside of the Pascal VOC dataset folder
# (the folder whose name is VOCdevkit).
# Run this file with 'dataset year' and 'class to be extracted'
# command line arguments. For example,
# python main.py 2007 person
#

import os
import random
import extract_class
from extract_class import abs_path
from extract_class import new_dir
from extract_class import args
from extract_class import extract_class

# Run extract_class function for extracting images and annotation files
extract_class()

#Train validation set to the proportion of the entire data set, modify it as needed
trainval_percent = 1
#The proportion of the training set to the training validation set, modify it as needed
train_percent = 0.7

xmlfilepath = os.path.join(abs_path, new_dir, 'Annotations/')
txtsavepath = os.path.join(abs_path, new_dir, 'ImageSets/Main/')
total_xml = os.listdir(xmlfilepath)

# Creates new directories for the extracted dataset
os.mkdir(os.path.join(abs_path, new_dir, 'ImageSets/'))
os.mkdir(txtsavepath)

num=len(total_xml)
list=range(num)
tv=int(num*trainval_percent)
tr=int(tv*train_percent)
trainval= random.sample(list,tv)
train=random.sample(trainval,tr)
 
ftrainval = open(txtsavepath+'/trainval.txt', 'w')
ftest = open(txtsavepath+'/test.txt', 'w')
ftrain = open(txtsavepath+'/train.txt', 'w')
fai_train = open(txtsavepath+'/{}_train.txt'.format(args.name), 'w')
fval = open(txtsavepath+'/val.txt', 'w')
fai_val = open(txtsavepath+'/{}_val.txt'.format(args.name), 'w')
fai_trainval = open(txtsavepath+'/{}_trainval.txt'.format(args.name), 'w')
 
for i  in list:
    name=total_xml[i][:-4]+'\n'
    ai_name=total_xml[i][:-4]+' 1'+'\n'
    if i in trainval:
        fname = name + ' ' + '1'
        ftrainval.write(name)
        fai_trainval.write(ai_name)
        if i in train:
            ftrain.write(name)
            fai_train.write(ai_name)
        else:
            fval.write(name)
            fai_val.write(ai_name)
    else:
        ftest.write(name)
 
ftrainval.close()
ftrain.close()
fval.close()
ftest .close()
