###############################################################
'''script used for interpolating gpx files to a dictionary.
   This is used for combining coordinated to detections based
   on timestamp'''
###############################################################

import gpxpy
import gpxpy.gpx
from datetime import datetime,timedelta
import time
import numpy as np
import pytz

import_gpx_file = open(r'gpx_files/janvanschoonvorststraat_adj.gpx')

# helper function for changing datetime to posix timestamp
def to_ts(dt):
    return time.mktime(dt.timetuple())

# helper function for changing posix timestamp to datetime
def to_dt(ts):
    return datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')


def gpx_interpolator(gpx_file):
    '''
    Function interpolating the gpx coordinated provided in the gpx file,
    retuning a dictionarry with interpolated coordinated for each second
    :param gpx_file:
    :return gpx_dict:
    '''
    # parse gpx file
    gpx = gpxpy.parse(gpx_file)

    # create empty list which will be filled by the gpx data
    lats=[]
    longs=[]
    times=[]

    #fill each list with gpx data
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                lats.append(point.latitude)
                longs.append(point.longitude)
                times.append(point.time.replace(microsecond=0)) # do not take microseconds into account

    # change times to posix timestamps
    times = list(map(lambda x: to_ts(x),times))

    # create an empty np array
    t = np.arange(times[0], times[-1])

    # the actual interpolation
    latint = np.interp(t, times, lats)
    lonint = np.interp(t, times, longs)

    # change times to posix timestamps
    t = list(map(lambda x: to_dt(x),t))

    # create a dict storing the time
    gpx_dict = dict(zip(t, zip(latint, lonint)))

    return gpx_dict

pos = gpx_interpolator(import_gpx_file)
a= pos

print(a)
