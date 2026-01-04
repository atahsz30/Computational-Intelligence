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
    testSize = math.floor(allNum * 0.2)
    return f[:trainSize], f[trainSize: trainSize + testSize]


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


def updateWeight(old, xx, yy):
    for i in range(len(old)):
        old[i] += xx[i] * yy
    return old


results = []
for i in range(10):
    print(f'\nrun {i + 1}:')
    Train_data, Test_data = DataLoader("DataSet.txt")
    bias = 0
    weight = 25 * [0]

    for x in Train_data:
        y = x[-1]
        weight = updateWeight(weight, x[:-1], y)
        bias += y
    wSt = ''
    for i in range(len(weight)):
        wSt += (str(weight[i]) + ",")
    wSt += str(bias)
    saveWeights("Hebb_weights.txt", wSt)
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
s = f'Hebb ( avg: {str(sum / 10)}, max: {results[9]}) \n'
f.write(s)
f.close()
