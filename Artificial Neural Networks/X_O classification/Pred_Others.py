address = {
    1: "Hebb_weights.txt",
    2: "Perceptron_weights.txt",
    3: "AdaLine_weights.txt",
}


def load_model(adr):
    f = open(adr, 'r')
    f = f.read()
    f = [float(i) for i in f.split(',')]
    return f[:-1], f[-1]


def prediction(x, m):
    weights, bias = load_model(address[m])
    res = 0
    for i in range(len(x)):
        res += weights[i] * x[i]
    res += bias
    return res
