import os
import glob

retrieve_path = r'C:\Users\JEbus\OneDrive - ilionx Group BV\ODK\Fotos\Roboflow\2021-03-24\labels_raw'
save_path = r'C:\Users\JEbus\OneDrive - ilionx Group BV\ODK\Fotos\Roboflow\2021-03-24\labels'

# get list of paths to all .txt files in folder
os.chdir(retrieve_path)
file_list = glob.glob('*.txt')

# key = class assigned to by RoboFlow, value = desired class
class_dict = {'4':'0', # container_small
              '6':'1', # garbage_bag
              '0':'2', # cardboard
              '9':'3', # matras 9
              '10':'4', # kerstboom 10
              '7':'5', # graffiti
              '11':'6', # amsterdammertje 11
              '5':'7', # face_privacy_filter
              '8':'8', # license_plate_privacy_filter
              '3':'9', # construction_toilet
              '1':'10', # construction_container
              '2':'11'} # construction_shed

# for-loop which ajust the class for each observation in each file based on the class_dict
for file in file_list:
    os.chdir(retrieve_path)
    with open(file, 'r') as read_file:
        lines = read_file.read().splitlines()

    os.chdir(save_path)
    with open(file,'w') as write_file:
        for item in lines:
            class_no = item[0]
            new_item = class_dict[class_no] + item[1:]
            write_file.write((new_item + '\n'))
