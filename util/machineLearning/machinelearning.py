from math import exp, log10

parameters = []
tsetX = [] # 2D array containing all x values of training set. len(tsetX) represents the total number of training sets (m)
tsetY = [] # 1D array with all training set y values
learning_rate = 2

def multiply_vectors(v1, v2):
    if (len(v1) != len(v2))
        print "===========vectors are not of same size!====================="
        return 0
    else
        ret_vector = []
        for i in range(len(v1)):
            ret_vector[i] = v1[i] * v2[i]
        return ret_vector

def cost_function():
    result = 0
    for r in range(len(tsetX)):
        hyp = calc_hypothesis(tsetX[r])
        tsetY[r] * log10(hyp) + (1 - tsetY[r]) * log10(1 - hyp)
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
    for i in range(len(parameters)):
        temp[i] = parameters[i] - learning_rate * partial_cost_function(i)
    parameters = temp

def calc_hypothesis(dataset):
    vector = multiply_vectors(parameters, dataset)
    result = 0
    for i in vector:
        result += i
    result = sigmoid(result)
    return result

def sigmoid(x):
    return 1.0/(1 + exp(-1 * x))

#def optimize(x):
#populate_parameters

def predict(inputX):
    int z = multiply_vectors(parameters, inputX)
    return sigmoid(z)
