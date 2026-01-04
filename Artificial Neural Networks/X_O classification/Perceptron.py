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
        prediction = 0
        for i in range(25):
            prediction += w[i] * xx[i]
        prediction += b
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
    bias = 0
    learning_R = 0.25
    theta = 0.2
    weight = 25 * [0]
    validAcc = []
    e = 0
    while True:
        e += 1
        miss = 0
        for x in Train_data:
            t = x[-1]
            y = 0
            for i in range(len(x) - 1):
                y += x[i] * weight[i]
            y += bias
            if y > theta:
                f_Y = 1
            elif -theta <= y <= theta:
                f_Y = 0
            else:
                f_Y = -1
            if f_Y != t:
                miss += 1
                weight = updateWeight(learning_R, weight, x[:-1], t)
                bias += learning_R * t
        validAcc.append(Test(weight, bias, Valid_data))
        if stopCondition(validAcc) or e >= 100:
            break

    wSt = ''
    for i in range(len(weight)):
        wSt += (str(weight[i]) + ",")
    wSt += str(bias)
    saveWeights("Perceptron_weights.txt", wSt)
    print("epochs: ", e)
    print("weights :", [*weight])
    print("bias: ", bias)
    acc = Test(weight, bias, Test_data)
    print(f'Test accuracy: {acc}')
    results.append(acc)
sum = 0
for i in range(10):
    sum += results[i]
results = sorted(results)

f = open("../Models Comparison.txt", 'a')
s = f'Perceptron ( avg: {str(sum / 10)}, max: {results[9]}) \n'
f.write(s)
f.close()
