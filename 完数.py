for i in range(1000):
    b=[]
    for j in range(1,i):
        if i%j==0:
            b.append(j)
    if i==sum(b):
        print(i)


