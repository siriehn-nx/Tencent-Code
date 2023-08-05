import numpy as np
import itertools
import tensorcircuit as tc
import matplotlib.pyplot as plt
c = tc.Circuit(2)
c.h(0)
c.cnot(0,1)
c.draw(output="mpl")
c.expectation([tc.gates.z() , [0]] , [tc.gates.z() , [1]])