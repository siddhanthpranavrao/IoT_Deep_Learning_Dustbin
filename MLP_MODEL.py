from sklearn.model_selection import train_test_split
from keras.utils import to_categorical
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics.classification import accuracy_score
import os
import glob
import csv
from sklearn.model_selection import train_test_split
from keras.layers import Dropout
from sklearn.preprocessing import LabelEncoder
from keras.optimizers import Adam
from keras import Sequential
from keras.layers import Dense
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn import metrics
from mypackage import extract_data as Ex
from sklearn.metrics import plot_confusion_matrix
import matplotlib
matplotlib.rcParams.update({'font.size': 20})




X_train, Y = Ex.extract()


Y = to_categorical(Y)

column_values = ['deviceID', 'Day', 'Time']

# creating the dataframe
X_train = np.array(X_train)
Y = np.array(Y)
df = pd.DataFrame(data=X_train,
                  columns=column_values)
x_train, x_test, y_train, y_test = train_test_split(
    df, Y, test_size=0.2, random_state=0,shuffle=True)




# creating a list of index names




# displaying the dataframe
model = Sequential()

model.add(Dense(30, activation='relu', input_shape=(3,)))
model.add(Dense(25, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(20, activation='relu'))
model.add(Dense(20, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(15, activation='relu'))
model.add(Dense(3, activation='softmax'))

adam = Adam(learning_rate=0.0015)
model.compile(loss='categorical_crossentropy', optimizer= adam, metrics=['accuracy'])

model.fit(
        x_train,
        y_train,
        nb_epoch=95,
        shuffle=True,
        verbose=1,
        validation_data=(x_test, y_test),
        validation_split=0.2

    )

y_pred = model.predict(x_test)
#y_pred = (y_pred > 0.5)
#
#target_names = ["LOW-LEVEL","HALF-LEVEL", "HIGH-LEVEL"]
labels = [0, 1 , 2]
# print(classification_report(y_test, y_pred, target_names=target_names))
model.save(r'C:\Users\praop\Desktop\Research\SMART_GARBAGE\CODES\mlp_model.h5')
#print(history.history.keys())



cm = confusion_matrix(y_test.argmax(axis=1), y_pred.argmax(axis=1),labels=labels)
print(cm)
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(cm)
plt.title('Confusion matrix of the classifier')
fig.colorbar(cax)
ax.set_xticklabels([''] + labels)
ax.set_yticklabels([''] + labels)
plt.xlabel('Predicted')
plt.ylabel('True')
plt.show()