import os
import glob

path = r'C:\Users\JEbus\OneDrive - ilionx Group BV\ODK\Fotos\Roboflow\images'

# get list of paths to all .jpg files in folder
os.chdir(path)
file_list = glob.glob('*.jpg')

# write each path to image in the vm folder in a .txt file
with open('garb_test.txt', 'a') as the_file:
    for i in file_list:
        path_name= './data_12/images/'+i
        print(path_name)
        the_file.write((path_name+ '\n'))