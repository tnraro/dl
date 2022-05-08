import numpy as np

def getData():
  y = np.array([81, 93, 91, 97])
  x1 = np.array([2, 4, 6, 8])
  x2 = np.array([0, 4, 2, 3])

  return y, x1, x2

def getDataForKeras():
  y = np.array([81, 93, 91, 97])
  x = np.array([[2, 0], [4, 4], [6, 2], [8, 3]])

  return y, x