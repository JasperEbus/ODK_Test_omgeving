import os
import glob
import cv2

path = r'C:\Users\JEbus\OneDrive - ilionx Group BV\ODK\Fotos\Roboflow\2021-03-24\images'

# get list of paths to all .jpg files in folder
os.chdir(path)
file_list = glob.glob('*.jpg')

# write each path to image in the vm folder in a .txt file
with open('garb_test.txt', 'a') as the_file:
    for i in file_list:
        path_name= './data_12/images/'+i
        print(path_name)
        the_file.write((path_name+ '\n'))

# get the width and height of an image and write in a .txt file

with open('garb_test.names', 'a') as the_file:
    for i in file_list:
        im = cv2.imread(i)
        h, w, c = im.shape
        dimensions = str(w) + ' ' + str(h)
        print(dimensions)
        the_file.write((dimensions + '\n'))