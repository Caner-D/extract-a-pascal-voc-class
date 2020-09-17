#
# Put this file inside of the Pascal VOC dataset folder
# (the folder whose name is VOCdevkit).
#

from image_annotation_extractor import args
def label_generator():
    text = "item {\
    \n  id: 1\
    \n  name: '"+args.name+"'\
    \n}"

    f = open("pascal_label_map.pbtxt", "w")
    f.write(text)
    f.close()

