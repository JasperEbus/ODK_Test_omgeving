###############################################################
'''test scipts for turning a video into frames'''
###############################################################
import cv2
import argparse


# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", required=True,
	help="path to input video file")
args = vars(ap.parse_args())

vidcap = cv2.VideoCapture(args["video"])

def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        cv2.imwrite("images\image"+str(count)+".jpg", image)     # save frame as JPG file
    return hasFrames,image

sec = 0
frameRate = 1/3 #//it will capture image in each 0.5 second
count=1
success = getFrame(sec)

print(success[0])
print(success[1])
print(success)
while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)