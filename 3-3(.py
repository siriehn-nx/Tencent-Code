import numpy as np
import math
import matplotlib.pyplot as plt

X = np.array([[[0, 1], [1, 0]], [[0, -1j],[1j, 0]], [[1, 0], [0, -1]]])
v0 = np.array([1, 0])
eps = 0.0000001
def exp(a, b):
  # a 参数一表示矩阵, b 参数表示 theta, 此函数为了计算 e ^ {i\theta P}
  return math.cos(b) * np.array([[1, 0], [0, 1]]) + 1j * math.sin(b) * a
def f(t, i, j):
    # i, j 相同的情况
	if i == j:
		return v0.conj() @ X[i] @ v0
	else:
		return v0.conj() @ -exp(X[i], t) @ X[j] @ v0
def df(f, a):
	return (f(a + eps) - f(a - eps)) / 2 * eps
def calc(x):
	e = np.zeros((len(x),), dtype = float)
	for i in range(0, len(x)):
		e[i] = f(x[i]).real
	return e
Y = np.linspace(-np.pi, np.pi, 256)
A = calc(Y)
print(A);
plt.plot(Y, A)
plt.grid()
plt.show()