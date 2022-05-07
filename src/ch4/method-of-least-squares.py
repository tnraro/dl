import numpy as np
import data

x, y = data.getData()

meanx = np.mean(x)
meany = np.mean(y)

divisor = sum([(i - meanx)**2 for i in x])

dividend = 0
for i in range(len(x)):
  dividend += (x[i] - meanx) * (y[i] - meany)

a = dividend / divisor
b = meany - (meanx * a)

print("기울기: ", a)
print("y 절편: ", b)