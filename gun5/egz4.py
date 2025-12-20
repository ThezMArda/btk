import numpy as np
from numpy import random
import matplotlib.pyplot as plt

rast=random.randn(50)
plt.hist(rast)
plt.xlabel("deger")
plt.ylabel("kaç tane çıktığı")
ort=rast.mean()
plt.grid(True)
plt.axvline(ort,color="red")
plt.show()


