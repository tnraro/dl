import data
import numpy as np
import matplotlib.pyplot as plt

y, x = data.getData()

plt.scatter(x, y)
plt.show()

a = 0
b = 0

lr = 0.03

epochs = 2001

n = len(x)

for i in range(epochs):
  y_pred = a * x + b
  error = y - y_pred

  a_diff = 2 / n * sum(-x * error)
  b_diff = 2 / n * sum(-error)

  a -= lr * a_diff
  b -= lr * b_diff

  if i % 100 == 0:
    print("epoch=%.f, 기울기=%.04f, 절편=%.04f" % (i, a, b))

y_pred = a * x + b

plt.scatter(x, y)
plt.plot(x, y_pred, "r")
plt.show()
