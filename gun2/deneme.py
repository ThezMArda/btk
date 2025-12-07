from typing import Optional
def add(a:int,b:int,c: Optional[int]=None)-> int:
    if c is None:
        return a+b
    else:
        return a+b+c

print(add(1,2))
print(add(1,2,3))