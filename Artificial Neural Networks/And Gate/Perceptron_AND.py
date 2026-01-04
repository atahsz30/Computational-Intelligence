data = [[1, 1, 1], [1, 0, -1], [0, 1, -1], [0, 0, -1]]
w1 = w2 = b = 0
alpha = 1
teta = 0.2
epoch = 10
for i in range(epoch):
    print(f'epoch: {i + 1}')
    for j in range(len(data)):
        x1 = data[j][0]
        x2 = data[j][1]
        target = data[j][2]
        y = b + x1 * w1 + x2 * w2
        if y > teta:
            f_Y = 1
        elif -teta <= y <= teta:
            f_Y = 0
        else:
            f_Y = -1
        if f_Y != target:
            w1 += alpha * x1 * target
            w2 += alpha * x2 * target
            b += alpha * 1 * target
        print(f'w1: {w1}, w2: {w2}, bias: {b}, y: {y} ')
    print("-------------------------------")

while True:
    xx1, xx2 = [int(i) for i in input("Enter Inputs: ").split()]
    p = xx1 * w1 + xx2 * w2 + b
    if p > 0:
        print(1)
    else:
        print(-1)
