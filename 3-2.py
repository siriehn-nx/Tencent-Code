from matplotlib import pyplot as plt
import numpy as np
X = np.array([[[0, 1], [1, 0]], [[0, -1j],[1j, 0]], [[1, 0], [0, -1]]])

print(X[0] @ X[1] @ X[0])