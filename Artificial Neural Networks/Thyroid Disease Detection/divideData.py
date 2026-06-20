import math


def divide(adrIn, adrOut):
    f = open(adrIn, 'r')
    f = f.read()
    f = f.split("\n")
    allNum = len(f)
    print(allNum)
    d = open(adrOut, 'r')
    d = d.read()
    d = d.split("\n")
    return f, d, allNum


def fill(adrIn, adrOut, ini, outi, s, e):
    w = open(adrIn, 'w')
    o = open(adrOut, 'w')
    for i in range(s, e):
        w.write((ini[i] + "\n"))
        o.write((outi[i] + "\n"))
    w.close()
    o.close()


inD, outD, num = divide("InData.txt", "OutData.txt")
trainSize = math.floor(num * 0.8)
testSize = math.floor(num * 0.1)
validSize = math.floor(num * 0.1)
fill("TrainIn.txt", "TrainOut.txt", inD, outD, 0, trainSize)
fill("TestIn.txt", "TestOut.txt", inD, outD, trainSize, trainSize + testSize)
fill("ValidIn.txt", "ValidOut.txt", inD, outD, trainSize + testSize, len(inD))
