from math import exp


parameters = []
tsetX = [] # 2D array containing all x values of training set. len(tsetX) represents the total number of training sets (m)
tsetY = [] # 1D array with all training set y values
growth_rate = 2

def multiply_vectors(v1, v2):
    if (len(v1) != len(v2))
        return 0
    else
        ret_vector = []
        for i in range(len(v1)):
            ret_vector[i] = v1[i] * v2[i]
        return ret_vector

def cost_function(r, c):
    return (hypothesis(tsetX[r]) - tsetY[r]) * tsetX[r][c]

def partial_cost_function(i):
    result  = 0
    for r in range(len(tsetX)):
        result += cost_function(r, i)
    return result

def gradient_descent():
    temp = []
    for i in range(len(parameters)):
        temp[i] = parameters[i] - growth_rate * partial_cost_function(i)
    parameters = temp

def hypothesis(row):
    vector = multiply_vectors(parameters, tsetX[row])
    result = 0
    for i in vector:
        result += i
    return result

def sigmoid_function(x):
    return 1.0/(1 + exp(-1 * x))
