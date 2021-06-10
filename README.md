# ODK Test Omgeving

In this repo several pieces of code used in the testing phase of the ODK project are stored. Additionally, GPX-files are added to the repo.

## Short script descriptions
Script | Description
------------ | -------------
creation_date.py | Get creation data from video
images_to_video.py | Turning frames into a video
main.py | Visually compare the detections of ODK to manual annotations
read_frames_faster.py | reading frames of a video (fast rate)
read_frames_slow.py | reading frames of a video (slow rate)
Roboflow_adjust.py | Change classes from Roboflow format to ODK model format
Roboflow_sampler.py | Store annotations and metadata of Roboflow output
test_time.py | Interpolate gpx files to seconds
utils.py | Helper functions for main.py
video_to_images.py | Turning a video into frames
