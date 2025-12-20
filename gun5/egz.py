import numpy as np
from numpy import random

sayilar = np.array ([])

rast=random.randint(0,70,size =20)

sayilar=np.append(sayilar,[rast])
sayilar/=2

print(np.mean(sayilar))
print(sayilar[sayilar>30])