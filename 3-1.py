from matplotlib import pyplot as plt
import numpy as np
# import tensorcircuit as tc
import random
import math
eps = 1e-5
def df(f, x):
    return (f(x + eps) - f(x)) / eps
