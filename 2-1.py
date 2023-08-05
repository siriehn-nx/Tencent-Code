from matplotlib import pyplot as plt
import numpy as np
import tensorcircuit as tc
import random
import math

def exp(a, b):
  # a 参数一表示矩阵, b 参数表示 theta, 此函数为了计算 e ^ {i\theta P}
  return np.cos(b) * np.array([[1, 0], [0, 1]]) + 1j * np.sin(b) * a;