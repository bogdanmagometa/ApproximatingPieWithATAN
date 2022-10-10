import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)


def atan_1(x):
    return 1 / (1 + x**2)

def atan_2(x):
    return 2 * x / (1 + x**2)**2

def atan_3(x):
    return (-6 * x**4 - 4 * x**2 + 2)  / (1 + x**2)**4

def taylor(derivatives, point_of_expansion):
    def taylor_function(x):
        if isinstance(x, np.ndarray):
            expan = np.zeros(x.shape)
        else:
            expan = 0
        for degree, derivative in enumerate(derivatives):
            expan += derivative(point_of_expansion) * (x - point_of_expansion)**degree / math.factorial(degree)
        return expan
    return taylor_function

x = np.linspace(-2, 2, 1000)

ax.plot(x, np.arctan(x), label="arctan")
ax.plot(x, taylor([np.arctan, atan_1], 0)(x), label="2-degree", linestyle='-')
ax.plot(x, taylor([np.arctan, atan_1, atan_2], 0)(x), label="3-degree", linestyle='-.')
ax.plot(x, taylor([np.arctan, atan_1, atan_2, atan_3], 0)(x), label="4-degree", linestyle='--')
ax.scatter(1, math.pi/4, label=r'$\frac{\pi}{4}$')

plt.grid()
plt.legend()
plt.show()
