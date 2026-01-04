import random, math


def DataLoader(address):
    f = open(address, 'r')
    f = f.read()
    f = f.split("\n")
    f = f[0:-1]
    random.shuffle(f)
    for i in range(len(f)):
        f[i] = [int(i) for i in f[i].split(",")]
    allNum = len(f)
    trainSize = math.floor(allNum * 0.8)
    testSize = math.floor(allNum * 0.1)
    validSize = math.floor(allNum * 0.1)
    return f[:trainSize], f[trainSize: trainSize + testSize], f[trainSize + testSize:]


def saveWeights(address, ws):
    f = open(address, 'w')
    f.write(ws)
    f.close()


def Test(w, b, tSet):
    counter = 0
    for x in tSet:
        target = x[-1]
        xx = x[:-1]
        y = [0, 0]
        for i in range(2):
            for j in range(len(xx)):
                y[i] += w[i][j] * xx[j]
            y[i] += b[i]
            y[i] = (math.e ** y[i])
        prediction = 1 if (y[0] > y[1]) else -1
        if (prediction > 0 and target == 1) or (prediction < 0 and target == -1):
            counter += 1
    return counter / len(tSet)


def updateWeight(alpha_, old, xx, target):
    for i in range(len(old)):
        old[i] += alpha_ * xx[i] * target
    return old


def stopCondition(v):
    n = len(v)
    if n < 5: return False
    diff = 0
    for i in range(n - 1):
        diff += abs(v[i + 1] - v[i])
    if diff < 0.3:
        return True
    return False


results = []
for i in range(10):
    print(f'\nrun {i + 1}:')
    Train_data, Test_data, Valid_data = DataLoader("DataSet.txt")
    bias = [0, 0]
    tArr = [0, 0]
    learning_R = 0.25
    theta = 0.2
    weight = [[0 for i in range(25)] for j in range(2)]
    validAcc = []
    e = 0
    while 1:
        e += 1
        miss = 0
        for x in Train_data:
            t = x[-1]
            tArr = [t, -t]
            y = [0, 0]
            f_Y = [0, 0]
            for i in range(2):
                for j in range(len(x) - 1):
                    y[i] += x[j] * weight[i][j]
                y[i] += bias[i]
                if y[i] > theta:
                    f_Y[i] = 1
                elif -theta <= y[i] <= theta:
                    f_Y[i] = 0
                else:
                    f_Y[i] = -1
            if not (f_Y[0] == tArr[0] and f_Y[1] == tArr[1]):
                miss += 1
                for i in range(2):
                    weight[i] = updateWeight(learning_R, weight[i], x[:-1], tArr[i])
                    bias[i] += learning_R * tArr[i]
        validAcc.append(Test(weight, bias, Valid_data))
        if stopCondition(validAcc) or e >= 100: break

    wSt = ''
    for i in range(len(weight[0])):
        wSt += (str(weight[0][i]) + ",")
    wSt = wSt[:-1]
    wSt += "\n"
    for i in range(len(weight[1])):
        wSt += (str(weight[1][i]) + ",")
    wSt = wSt[:-1]
    wSt += f'\n{bias[0]},{bias[1]}'
    saveWeights("P_MultiCategory_weights.txt", wSt)
    print("epochs: ", e)
    print("weights(v): ", [*weight[0]])
    print("weights(w): ", [*weight[1]])
    print("bias: ", bias)
    acc = Test(weight, bias, Test_data)
    print(f'Test accuracy: {acc}')
    results.append(acc)
sum = 0
for i in range(10):
    sum += results[i]
results = sorted(results)

f = open("../Models Comparison.txt", 'a')
s = f'Multi Category Perceptron ( avg: {str(sum / 10)}, max: {results[9]}) \n'
f.write(s)
f.close()
