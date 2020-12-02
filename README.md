# Deep Learning Based Smart Garbage Monitoring System
Team Members: [Siddhanth P. Rao](https://github.com/siddhanthpranavrao), [Pratyaksh P. Rao](https://github.com/pratyaksh10), [Rohit Ranjan](https://github.com/rohit0709)

This research project contains three parts,

1. Data collection 

2. Model training 

3. Result analysis 

## Files 

- [`DataCollection`](DataCollection) : This folder contains an embedded C program to collect data from the ultrasonic sensor connected to ESP32. Moreover, data will be sent to Firebase and can be retreived by the host device.

- [`MLP_MODEL.py`](MLP_MODEL.py) : This python file contains a code that demonstrates the working of our proposed model. 

- [`PLOTTING.py`](PLOTTING.py) : The following python code is used to plot the confusion matrix of the proposed neural network model.

- [`predict.py`](predict.py) : Contains the code to predict future garbage levels of a smart dusbin on a given day and time.


## Dependensies

- [Tensorflow](http://tensorflow.org)

- [Keras](http://keras.io)

- [Arduino](https://www.arduino.cc)
