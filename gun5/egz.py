import numpy as np
from numpy import random

sayilar = np.array ([])

rast=random.randint(0,51,size =20)

sayilar=rast/2
print(sayilar)
print(np.mean(rast))
print(rast[rast>30])