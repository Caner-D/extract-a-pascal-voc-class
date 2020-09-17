# Put this module inside the folder which contains training labels folder and test labels folder
# Before using this split labels into training folder and test folder
# Usage: python csv_generator.py trainlabels testlabels

import os
import glob
import pandas
import xml.etree.ElementTree as ET
import argparse

# Creates command line arguments for ease of use
parser = argparse.ArgumentParser()
# Write folder name which contains annotation files
parser.add_argument('name', nargs='*')
args = parser.parse_args()

# Creates an array for mapping folder names with csv files
map_arr = ['train_labels', 'test_labels']

# Returns a csv file that contains image name, width, height, class, xmin, ymin, xmax, ymax values
def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            for box in member.findall('bndbox'):
                value = (root.find('filename').text,
                        int(root.find('size')[0].text),
                        int(root.find('size')[1].text),
                        member[0].text,
                        int(box[0].text),
                        int(box[1].text),
                        int(box[2].text),
                        int(box[3].text)
                        )
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pandas.DataFrame(xml_list, columns=column_name)
    return xml_df


def main():
    for dict_index, file in enumerate(args.name):
        image_path = os.path.join(os.getcwd(), file)
        xml_df = xml_to_csv(image_path)
        xml_df.to_csv("{}.csv".format(map_arr[dict_index]), index=None)
        print('Successfully converted xml to csv.')

main()