###############################################################
'''test scipts for turning frames into a video'''
###############################################################


import cv2
import numpy as np
import os
from os.path import isfile, join
import argparse

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True,
	help="path to input folder")
ap.add_argument("-o", "--output", required=True,
	help="path to output video file")
args = vars(ap.parse_args())

# pathIn = './images/'
fps = 3

frame_array = []
files = [f for f in os.listdir(args["input"]) if isfile(join(args["input"], f))]

# for sorting the file names properly
files.sort(key=lambda x: x[5:-4])

for i in range(len(files)):
    filename = args["input"] + files[i]
    # reading each files
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width, height)

    # inserting the frames into an image array
    frame_array.append(img)
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(args["output"],fourcc, fps, size)
for i in range(len(frame_array)):
    # writing to a image array
    out.write(frame_array[i])
out.release()