import math

hidden_neuron_num = 15
classNum = 2


def load_model(adr):
    f = open(adr, 'r')
    f = f.read()
    f = f.split('\n')
    f = f[:-1]
    w = []
    v = []
    for t in range(len(f)):
        f[t] = [float(i) for i in f[t].split(',')]
    for t in range(classNum):
        w.append(f[t])
    for t in range(classNum, classNum + hidden_neuron_num):
        v.append(f[t])
    w.append(f[classNum + hidden_neuron_num])
    v.append(f[classNum + hidden_neuron_num + 1])

    return w[:-1], w[-1], v[:-1], v[-1]


def prediction(x):
    w_weights, w_bias, v_weights, v_bias = load_model("MLP_weights.txt")
    z = [0 for _ in range(hidden_neuron_num)]
    y = [0 for _ in range(classNum)]
    for i in range(hidden_neuron_num):
        for j in range(len(x)):
            z[i] += v_weights[i][j] * x[j]
        z[i] += v_bias[i]
    for i in range(classNum):
        for j in range(len(z)):
            y[i] += w_weights[i][j] * z[j]
        y[i] += w_bias[i]
        y[i] = (math.e ** y[i])
    prediction = 1 if (y[0] > y[1]) else -1
    return prediction
