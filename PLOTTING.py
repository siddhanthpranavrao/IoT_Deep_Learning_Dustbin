import os
import glob
import pandas as pd
import numpy as np
import csv
from datetime import datetime
import matplotlib.pyplot as plt
import sys
import os

os.chdir(r'C:\Users\praop\Desktop\Research\SMART_GARBAGE\Dataset')


Y_train_2 = []


with open('dataset_bin2.csv', 'r') as file:
    reader = csv.reader(file)
    for data in reader:
        Y_train_2.append(int(data[3]))


Y_train_3 = []
with open('dataset_bin3.csv', 'r') as file:
    reader = csv.reader(file)
    for data in reader:
        Y_train_3.append(int(data[3]))

def my_function(x):
  return list(dict.fromkeys(x))




Y_train= []
eventTime = []
Date = []

with open('dataset_bin1.csv', 'r') as file:
    reader = csv.reader(file)
    for data in reader:
        eventTime.append(data[2])
        Y_train.append(int(data[3]))
        Date.append(data[1])

    attribute_time = []


    for time in eventTime:
        attribute_time.append(time.split(':')[0])

    avg_val = []
    avg_val_2 = []
    avg_val_3 = []


    Dates = []

    Dates = my_function(Date)



    for i in range(int(len(Y_train)/24)):

        lower_limit = i*24
        upper_limit = lower_limit + 24
        avg_val.append(sum(Y_train[lower_limit:upper_limit])/ 24)
        avg_val_2.append(sum(Y_train_2[lower_limit:upper_limit])/ 24)
        avg_val_3.append(sum(Y_train_3[lower_limit:upper_limit]) / 24)


    x = Dates

    y = avg_val

    z = avg_val_2

    k = avg_val_3

    plt.plot(x, y, x, z,x,k)

    plt.xticks(rotation=45)
    plt.xlabel('Date')
    plt.ylabel('GarbageLevels (cm)')
    plt.title('GarbageLevels vs Date')

    plt.show()





























