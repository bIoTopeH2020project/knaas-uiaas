import numpy as np
import matplotlib as plt

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()
