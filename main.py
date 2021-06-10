###############################################################
'''Script for simple visually comparing the ODK models,
   The findings are compared to the baseline - manually
   created annotations using Roboflow'''
###############################################################

import json
import glob
import os
import pandas as pd
from utils import *

model_output_paths = ['output_ehv_20210301_3_classes',
                      'output_ehv_20210301_12_classes_10000',
                      'output_ehv_20210301_12_classes_40000']
manual_output_file = 'handmatige_classificatie2.csv'

def main(model_lst,manual_file):
    df_lst=[]
    for path in model_lst:
        df_lst.append(sum_df(model_df_creater(path)))
    df_lst.append(sum_df(manual_df_creator(manual_file)))

    create_bar_chart(df_lst)

if __name__ == "__main__":
    main(model_output_paths,manual_output_file)