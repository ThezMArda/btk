import numpy as np
from numpy import random
import matplotlib.pyplot as plt

rast=random.randn(50)
plt.hist(rast,alpha=0.7)
plt.xlabel("deger")
plt.ylabel("kaç tane çıktığı")
ort=rast.mean()
plt.grid(True)
plt.axvline(ort,color="red",linestyle="--",label=f"Ortalama degeri{ort}")
plt.legend()

plt.show()


