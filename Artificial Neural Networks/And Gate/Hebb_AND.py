import matplotlib.pyplot as plt

data = [[1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, -1]]
w1 = w2 = b = 0
alpha = 1
teta = 0.2
epoch = 1
for j in range(len(data)):
    x1 = data[j][0]
    x2 = data[j][1]
    target = data[j][2]
    w1 += x1 * target
    w2 += x2 * target
    b += target
    ml = -w1 / w2
    cl = -b / w2
    xl = []
    yl = []
    for i in range(-10, 10):
        xl.append(i)
        yl.append(ml * i + cl)
    print(f'w1: {w1}, w2: {w2}, bias: {b}')
    plt.plot(xl, yl, color='red', linewidth=3)
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)
    plt.xlim(-5, 5)
    plt.ylim(-5, 5)
    plt.grid(True)
    plt.show()
print("-------------------------------")

while True:
    xx1, xx2 = [int(i) for i in input("Enter Inputs: ").split()]
    p = xx1 * w1 + xx2 * w2 + b
    if p > 0:
        print(1)
    else:
        print(-1)
