from math import exp, log
import numpy as np
from scipy.optimize import minimize

# n_arr: dataset
# tsetX: an array that you want the x values of the dataset to be stored
# tsetY: an array that you want the y values of the dataset to be stored
# tsetX and tsetY will be filled with the properly parsed data from dataset
def set_train_set(n_arr, tsetX, tsetY):
    len_arr = len(n_arr)
    for r in range(len_arr):
        append_train_set(n_arr[r], tsetX, tsetY)
    # print "tset1\n", tsetX
    # print "tset2\n", tsetY

# arr: an array of data you want to add
# tsetX: an array that you want the x values of the dataset to be stored
# tsetY: an array that you want the y values of the dataset to be stored
def append_train_set(arr, tsetX, tsetY):
    arr.insert(0, 1) # adds y intercept at 0th index
    tsetX.append(arr[:len(arr) - 1])
    tsetY.append(arr[len(arr) - 1])
    # print arr

# returns a 0 vector with the proper length
# length is determined by the dataset
def populate_parameters(tsetX):
    parameters = []
    for i in range(len(tsetX[0])):
        parameters.append(0) #(random() * 10)
    return parameters
    # print "parameters:", parameters
    # print "\n"

# sigmoid function
def sigmoid(x):
    return 1.0/(1.0 + exp(-1 * x))

# parameters: vector of points
# tsetX: dataset of x values
# tsetY: dataset of y values
# cost function for logistic regression:
def cost_function(parameters, tsetX, tsetY):
    result = 0
    for r in range(len(tsetX)):
        hyp = sigmoid(np.dot(parameters, tsetX[r]))
        if (hyp == 1): # prevent domain error
            hyp = .99999999999
        result += tsetY[r] * log(hyp) + (1 - tsetY[r]) * log(1 - hyp)
    result *= -1/len(tsetX)
    return result

# minimizes the cost function with respect to theta/parameters
def optimize(parameters, tsetX, tsetY):
    return minimize(cost_function, parameters , args=(tsetX, tsetY))

# runs the proper setup for the data and parameters
def setup(data, tsetX, tsetY):
    set_train_set(data, tsetX, tsetY)
    p = populate_parameters(tsetX) #[0, 0, 0]
    return p

# returns the proper parameters given by the minimize function
def optimize_parameters(parameters, tsetX, tsetY):
    t = optimize(parameters, tsetX, tsetY)
    return t.x # array of parameters

# takes in an input and returns probability of the data being in the "1" state
def predict(parameters, x):
    x.insert(0, 1) # add intercept
    return sigmoid(np.dot(parameters, x))
