import math
classNum = 2


def load_model(adr):
    f = open(adr, 'r')
    f = f.read()
    f = f.split('\n')
    for t in range(len(f)):
        f[t] = [float(i) for i in f[t].split(',')]
    return f[:-1], f[-1]


def prediction(x):
    weights, bias = load_model("P_MultiCategory_weights.txt")
    y = [0 for i in range(classNum)]
    for i in range(2):
        for j in range(len(x)):
            y[i] += weights[i][j] * x[j]
        y[i] += bias[i]
        y[i] = (math.e ** y[i])
    prediction = 1 if (y[0] > y[1]) else -1
    return prediction

