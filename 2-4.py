from matplotlib import pyplot as plt
import numpy as np
# import tensorcircuit as tc
import random
import math

'''
poly matrix
X. 
[[0, 1],[1, 0]]
Z. 
[[1, 0],[0, -1]]
'''
X = np.array([[0, 1],[1, 0]])
Z = np.array([[1, 0],[0, -1]])
n = int(input())
I = np.array([[1, 0], [0, 1]])
ans = np.zeros(shape = [2 ** n, 2 ** n], dtype=float)
for i in range (0, n):
	a = np.array([1], dtype=float)
	for j in range(0, i):
		a = np.kron(a, I)
	a = np.kron(a, Z)
	for j in range (i + 1, n):
		a = np.kron(a, I)
	ans += a
for i in range (0, n - 1):
	a = np.array([1], dtype=float)
	for j in range(0, i):
		a = np.kron(a, I)
	a = np.kron(a, X)
	a = np.kron(a, X)
	for j in range (i + 2, n):
		a = np.kron(a, I)
	ans += a
print(ans)
H = np.zeros(2 ** n)
H[0] = 1;
dans = H.conj().T @ ans @ H;
print(dans)