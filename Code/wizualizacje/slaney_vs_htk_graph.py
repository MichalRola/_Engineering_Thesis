import os
import numpy as np
import matplotlib.pyplot as plt

f = np.linspace(16, 20000, 2000)

slaney = []

for i in f:
    if i < 1000:
        slaney.append(3*i/200)
    elif i >= 1000:
        slaney.append(1527*np.emath.logn(6.4, i/1000))

HTK = 2595*np.log10((1+f)/700)

plt.plot(f, slaney, 'k-', linewidth=2)
plt.plot(f, HTK, 'k--', linewidth=2)
plt.legend(['Slaney', 'HTK'])
plt.xlabel("Herce [Hz]")
plt.ylabel("Mele [mel]")
plt.xlim(0, 20000)
plt.ylim(0, 4000)
plt.savefig(os.path.join(r'D:\Folders\_Engineering_Thesis\Papers\Images', 'slaney_vs_HTK.png'))
plt.show()
