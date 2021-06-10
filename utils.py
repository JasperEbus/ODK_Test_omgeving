###############################################################
'''Halper functions for main.py'''
###############################################################

import pandas as pd
import json
import glob
import os
import plotly.graph_objects as go


base_dir = r'C:\Users\JEbus\OneDrive - ilionx Group BV\ODK\ODK test Ehv\output'
column_headers = ['IID',
                  'weights',
                  'container_small',
                  'garbage_bag',
                  'cardboard',
                  'matras',
                  'christmas_tree',
                  'graffiti',
                  'pole',
                  'face_privacy_filter',
                  'license_plate_privacy_filter',
                  'construction_toilet',
                  'construction_container',
                  'construction_shed']

def model_df_creater(folder):
    path = os.path.join(base_dir, folder)
    os.chdir(path)
    json_list = glob.glob('*.json')
    df = pd.DataFrame(columns=column_headers)

    for file in json_list:
        with open(file) as json_file:
            summary = {'IID': file[:15],
                       'weights': folder}
            data = json.load(json_file)
            detections = data['detections']
            for i in range(len(detections)):
                detection = detections[i]['class']
                if detection in summary.keys():
                    summary[detection] += 1
                else:
                    summary[detection] = 1
            df = df.append(summary, ignore_index=True)
    return df


def manual_df_creator(file):
    path = os.path.join(base_dir, file)
    df = pd.read_csv(path, ';')
    return df


def sum_df(df):
    df_sum = pd.DataFrame(columns=['weights','detection_type','detections'])
    weight = df['weights'][0]
    for detection_type in column_headers[2:]:
        sum_val = df[detection_type].sum()
        summary ={'weights':weight,'detection_type':detection_type,'detections':sum_val}
        df_sum = df_sum.append(summary, ignore_index=True)
    return df_sum

def create_bar_chart(df_list):
    fig = go.Figure()
    for df in df_list:
        fig.add_trace(go.Bar(
            x=df['detection_type'],
            y=df['detections'],
            name=df['weights'][0]
        ))
    fig.show()
