# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 05:10:01 2017

@author: wc57661
"""

import numpy as np
import csv
import os
import re

cwd=os.getcwd()

#input
input_file_name='try_csv.csv'
output_file_name='output_date.csv'
output_histo_file_name='output_date_histo.csv'

#import
raw_data=[]
with open(input_file_name, mode='r') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in reader:
        raw_data.append(row)
col1=[]
col2=[]
col3=[]
col4=[]
for row in raw_data:
    a=re.split(',',row[0])
    col1.append(a[0])
    col2.append(a[1])
    col3.append(a[2])
    col4.append(a[3])        
raw_data_size=len(raw_data)
#raw_data=np.asarray(raw_data)
col_size=len(col1)
