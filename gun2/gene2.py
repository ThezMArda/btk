def carptablo():
    for i in range (1,11):
        for j in range (1,11):
            yield(f"{i} * {j} = {i*j}")
for i in carptablo():
    print (i)
