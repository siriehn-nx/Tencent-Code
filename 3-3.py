import numpy as np
import math
import tensorcircuit as tc
from matplotlib import pyplot as plt
v=np.array([1,0])
def exp(a, b):
    q=math.cos(b) * np.array([[1, 0], [0, 1]]) + 1j * math.sin(b) * a
    return q
def f(b):
    a=np.array([[0,1],[1,0]])
    c_1=(exp(a,b)@v)  
    d_1=(np.array([[1,0],[0,-1]])@c_1)
    e_1=(c_1.conj().T @d_1)
    c_2=(exp(a,b*1.00001)@v)  
    d_2=(np.array([[1,0],[0,-1]])@c_2)
    e_2=(c_2.conj().T @d_2)
    q=(e_2-e_1)/(0.00001*b)
    return q
b=np.linspace(-2*math.pi,2*math.pi,100)
y = [f(b) for b in b]
plt.plot(b,y)
plt.show()