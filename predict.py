from keras.models import load_model
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import os
from sklearn.model_selection import train_test_split
import numpy as np
import csv
from keras.utils import to_categorical
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.metrics import plot_confusion_matrix
from sklearn.model_selection import train_test_split
from mypackage import extract_data as Ex


X_train, Y = Ex.extract()
os.chdir(r'C:\Users\praop\Desktop\Research\SMART_GARBAGE\CODES')

Y = to_categorical(Y)

column_values = ['deviceID', 'Day', 'Time']

# creating the dataframe
X_train = np.array(X_train)
Y = np.array(Y)
df = pd.DataFrame(data=X_train,
                  columns=column_values)
x_train, x_test, y_train, y_test = train_test_split(
    df, Y, test_size=0.2, random_state=0,shuffle=True)
model = load_model(r'C:\Users\praop\Desktop\Research\SMART_GARBAGE\CODES\mlp_model.h5')
model.fit(X_train,y_train)

# id = int(input("ENTER BIN ID"))
# day = int(input("ENTER DAY"))
# time = int(input("ENTER TIME"))



X_test = [0, 1, 11]
X_test = np.array(X_test).astype(np.int)
X_test = X_test.reshape(1, -1)
y_pred = model.predict(X_test)

# prediction = y_pred.round(2)
# print(prediction)

plot_confusion_matrix(model, X_test, y_test)  # doctest: +SKIP
plt.show()


