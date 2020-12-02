import numpy as np

x = np.array([[1, 0, 0, 1],  # INPUT
              [0, 0, 1, 1],
              [1, 1, 1, 0],
              [0, 0, 1, 1]], dtype='float64')

y = np.array([0, 1, 1, 1]).T  # OUTPUT


def relu(x, diff=False):  # ACTIVATION FUNCTION
    if diff == True:
        return (x > 0)
    return (x > 0) * x


np.random.seed(3)


def initialize_weights():
    parameters = {}

    parameters['W1'] = 2 * np.random.randn(3, 4) - 1  # 3 x 4
    parameters['b1'] = np.zeros((3, 1))  # b -> 3 x 1
    parameters['W2'] = 2 * np.random.randn(1, 3) - 1  # 1 x 3
    parameters['b2'] = np.zeros((1, 1))  # b -> 1 x 1

    return parameters


parameters = initialize_weights()

print("Shape of W1:", parameters['W1'].shape)
print("Shape of W2:", parameters['W2'].shape)
print("Shape of b1:", parameters['b1'].shape)
print("Shape of b1:", parameters['b2'].shape)
print("Shape of x:", x.shape)
print("Shape of y:", y.shape)

print("WEIGHTS AND BIASES BEFORE TRAINING:")
print(parameters)


def forward_propagation(parameters):
    layer_1 = relu(np.dot(parameters['W1'], x) + parameters['b1'], diff=False)
    layer_2 = np.dot(parameters['W2'], layer_1) + parameters['b2']

    return layer_1, layer_2


def back_propagation(learning_rate, x, y, layer_1, layer_2):
    delta_layer_2 = (layer_2 - y)  # 1x4
    delta_layer_1 = np.dot(parameters['W2'].T, delta_layer_2) * relu(np.dot(parameters['W1'], x) + parameters['b1'],
                                                                     diff=True)  # 3x4
    db_2 = (1 / 4) * np.sum(delta_layer_2, axis=1, keepdims=True)
    db_1 = (1 / 4) * np.sum(delta_layer_1, axis=1, keepdims=True)

    dw_2 = np.dot(delta_layer_2, layer_1.T)
    dw_1 = np.dot(delta_layer_1, x.T)

    parameters['W1'] -= learning_rate * dw_1
    parameters['W2'] -= learning_rate * dw_2
    parameters['b1'] -= learning_rate * db_1
    parameters['b2'] -= learning_rate * db_2

    return parameters


learning_rate = 0.01
# TRANING THE MODEL
for iter in range(10000):  # No. of epochs

    layer_1, layer_2 = forward_propagation(parameters)
    parameters = back_propagation(0.01, x, y, layer_1, layer_2)

print("WEIGHTS AND BIASES AFTER TRAINING:")
print(parameters)
print("prediction :")
print(layer_2)
print("actual y")
print(y)