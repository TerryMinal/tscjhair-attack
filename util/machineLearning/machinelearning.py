from math import exp, log10
from random import random
from sys import exit
parameters = []
tsetX = [] # 2D array containing all x values of training set. len(tsetX) represents the total number of training sets (m)
tsetY = [] # 1D array with all training set y values
learning_rate = .04

def error_check(i, message):
    if (i == 0):
        print "ERROR: " + message + "\nexiting program..."
        exit()
    else:
        return 1

# pass in a 2D array
def set_train_set(n_arr):
    len_arr = len(n_arr)
    len_inner = len(n_arr[0])
    for r in range(len_arr):
        append_train_set(n_arr[r])
    # print "tset1\n", tsetX
    # print "tset2\n", tsetY

# pass in a 1D array to be added existing training set
def append_train_set(arr):
    tsetX.append(arr[:len(arr) - 1])
    tsetY.append(arr[len(arr) - 1])
    # print arr

def populate_parameters():
    for i in range(len(tsetX[0])):
        parameters.append((random() + 1) * 3)
    # print "parameters:", parameters
    # print "\n"

def multiply_vectors(v1, v2):
    if (len(v1) != len(v2)):
        print "===========ERROR: vectors are not of same size!====================="
        exit()
    else:
        ret_vector = []
        for i in range(len(v1)):
            ret_vector.append(v1[i] * v2[i])
        return ret_vector

def cost_function():
    result = 0
    for r in range(len(tsetX)):
        hyp = calc_hypothesis(tsetX[r])
        if (hyp == 1): # to prevent domain error
            hyp = .9999999
        # print "hyp", hyp
        # print "tsetY", tsetY[r]
        result += tsetY[r] * log10(hyp) + (1 - tsetY[r]) * log10(1 - hyp)
    result *= -1/len(tsetX)
    return result

def partial_cost_function(i):
    result  = 0
    for r in range(len(tsetX)):
        result += (calc_hypothesis(tsetX[r]) - tsetY[r]) * tsetX[r][i]
    result = 1.0/len(tsetX) * result
    return result

# obtains the gradient descent of the cost function
def gradient_descent():
    temp = []
    global parameters
    for i in range(len(parameters)):
        temp.append(parameters[i] - learning_rate * partial_cost_function(i))
    parameters = temp
    print "parameters", parameters

def calc_hypothesis(dataset):
    # print "length of parameters", len(parameters)
    # print "length of dataset", len(dataset)
    vector = multiply_vectors(parameters, dataset)
    # error_check(vector, "vector is 0")
    # print "vector", vector
    result = 0
    for i in vector:
        result += i
    # print "result before sigmoid implementation:", result
    result = sigmoid(result)
    # print "result after sigmoid", result
    return result

def sigmoid(x):
    # print "sigmoiding", 1.0/(1.0 + exp(-1 * x))
    return 1.0/(1.0 + exp(-1 * x))

def optimize():
    old_num = cost_function()
    gradient_descent()
    new_num = cost_function()
    iterations = 0
    while (new_num <= old_num):
        print "iteration: ", iterations
        old_num = new_num
        gradient_descent()
        new_num = cost_function()
        iterations += 1
    # if (iterations == 400):
    #     print "maximum iterations reached... terminating optimization"
    print "minimum", old_num
    print parameters
    return old_num

def predict(inputX):
    z = multiply_vectors(parameters, inputX)
    n = 0
    for i in z:
        n += i
    n = sigmoid(n)
    return n
    # if (n >= .5):
    #     return
