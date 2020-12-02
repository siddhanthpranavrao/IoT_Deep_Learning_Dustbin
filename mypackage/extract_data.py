import os
import glob
import csv


deviceId = []
day = []
Y_train = []
eventTime = []

os.chdir(r'C:\Users\praop\Desktop\Research\SMART_GARBAGE\Dataset')


def extract():


    with open('dataset.csv', 'r') as file:
        reader = csv.reader(file)
        for data in reader:
            day.append(data[0])
            eventTime.append(data[2])
            Y_train.append(int(data[3]))
            deviceId.append(data[4])

        attribute_time = []

        for time in eventTime:
            attribute_time.append(time.split(':')[0])

        X_train = []
        data_len = len(day)

        for i in range(data_len):
            x = []
            x.append(deviceId[i])
            x.append(day[i])
            x.append(attribute_time[i])

            X_train.append(x)

        Y = []

        for i in Y_train:
            if i >= 35:
                Y.append(2)
            elif i >= 15 and i < 35:
                Y.append(1)

            else:
                Y.append(0)

    return X_train, Y