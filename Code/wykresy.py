import numpy as np
import matplotlib.pyplot as plt

f = np.linspace(16, 20000, 2000)

HTK = 2595*np.log10((1+f)/700)

slaney = []

for i in f:
    if i < 1000:
        slaney.append(3*i/200)
    elif i >= 1000:
        slaney.append(1527*np.emath.logn(6.4, f/1000))

plt.plot(HTK, f)
plt.show()

plt.plot(slaney, f)