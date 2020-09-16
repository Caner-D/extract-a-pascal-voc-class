#
# Put this file inside of the Pascal VOC dataset folder
# (the folder whose name is VOCdevkit).
#

import os
import shutil
import argparse

# Creates command line arguments for ease of use
parser = argparse.ArgumentParser()
# Pick a year for the dataset
parser.add_argument('year')
# Select class to be extracted from dataset
parser.add_argument('name')
args = parser.parse_args()

# Creates year dictionary for the dataset
dict_year =	{
'2007': 'VOC2007',
'2012': 'VOC2012',
}

# File paths for future operations
abs_path = os.path.abspath("")
new_dir = "VOCdevkit/" + dict_year[args.year]

def extract_class():
    # Creates new directories for the extracted dataset
    os.mkdir("VOCdevkit")
    os.mkdir("VOCdevkit/" + dict_year[args.year])

    ann_filepath= os.path.join(abs_path, dict_year[args.year], 'Annotations/')
    img_filepath= os.path.join(abs_path, dict_year[args.year], 'JPEGImages/')
    ann_savepath= os.path.join(abs_path, new_dir, 'Annotations/')
    img_savepath= os.path.join(abs_path, new_dir, 'JPEGImages/')
    if not os.path.exists(img_savepath):
        os.mkdir(img_savepath)
    
    if not os.path.exists(ann_savepath):
        os.mkdir(ann_savepath)
    names = locals()
    classes = ['aeroplane','bicycle','bird', 'boat', 'bottle',
            'bus', 'car', 'cat', 'chair', 'cow','diningtable',
            'dog', 'horse', 'motorbike', 'pottedplant',
            'sheep', 'sofa', 'train', 'tvmonitor', 'person']

    for file in os.listdir(ann_filepath):
        print(file)
        fp = open(ann_filepath + '//' + file)
        ann_savefile=ann_savepath+file
        fp_w = open(ann_savefile, 'w')
        lines = fp.readlines()

        ind_start = []
        ind_end = []
        lines_id_start = lines[:]
        lines_id_end = lines[:]

        class_sel = '\t\t<name>{}</name>\n'.format(args.name)
    
        #Found the object block in xml and record it
        while "\t<object>\n" in lines_id_start:
            a = lines_id_start.index("\t<object>\n")
            ind_start.append(a)
            lines_id_start[a] = "delete"
    
    
        while "\t</object>\n" in lines_id_end:
            b = lines_id_end.index("\t</object>\n")
            ind_end.append(b)
            lines_id_end[b] = "delete"
    
        #Names stores all object blocks
        i = 0
        for k in range(0, len(ind_start)):
            names['block%d' % k] = []
            for j in range(0, len(classes)):
                if classes[j] in lines[ind_start[i] + 1]:
                    a = ind_start[i]
                    for o in range(ind_end[i] - ind_start[i] + 1):
                        names['block%d' % k].append(lines[a + o])
                    break
            i += 1 
    
        #xml 
        string_start = lines[0:ind_start[0]]
        #xml 
        string_end = [lines[len(lines) - 1]]
    
    
        # Search in the given class, if it exists, write the object block information
        a = 0
        for k in range(0, len(ind_start)):
            if class_sel in names['block%d' % k]:
                a += 1
                string_start += names['block%d' % k]  
        string_start += string_end
        for c in range(0, len(string_start)):
            fp_w.write(string_start[c])
        fp_w.close()
        #If there is no module we are looking for, delete this xml, if you copy the picture
        if a == 0:
            os.remove(ann_savepath+file)
        else:
            name_img = img_filepath + os.path.splitext(file)[0] + ".jpg"
            shutil.copy(name_img, img_savepath)
        fp.close()

if __name__ == '__main__':
    extract_class()
