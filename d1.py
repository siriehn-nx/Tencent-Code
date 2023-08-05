from matplotlib import pyplot as plt
import numpy as np
# import tensorcircuit as tc
import random
import math

'''
poly matrix
1. 
[[0, 1],[1, 0]]
2. 
[[0, -i],[i, 0]]
3. 
[[1, 0],[0, -1]]
'''
X = np.array([[[0, 1], [1, 0]], [[0, -1j],[1j, 0]], [[1, 0], [0, -1]]])
v0 = np.array([[1], [0]])
def exp(a, b):
  # a 参数一表示矩阵, b 参数表示 theta, 此函数为了计算 e ^ {i\theta P}
  return math.cos(b) * np.array([[1, 0], [0, 1]]) + 1j * math.sin(b) * a;
def calc(a, b, c):
  # a 参数一表示第一个矩阵 P, b 参数二表示第二个矩阵 Q, c 参数三表示 theta
  d = np.zeros((len(c), 2, 1))
  e = np.zeros((len(c),))
  for i in range(0, len(c)):
    d[i] = np.matmul(exp(X[a], c[i] / 2), v0)
    if (d[i].all() != np.matmul(exp(X[a], c[i] / 2), v0).all()):
      print("NO")
  for i in range(0, len(d)):
    print((d[i].conj().T @ X[b] @ d[i])[0][0].real)
  return e
Y = np.linspace(-np.pi, np.pi, 256)
A = calc(0, 1, Y)
# print(A);
plt.plot(Y, A)
plt.grid()
plt.show()

  