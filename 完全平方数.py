import math

for i in range(-100,10000):
    m1=math.sqrt(i+100)
    m2=math.sqrt(i+100+168)
    if m1==int(m1):
        if m2==int(m2):
            print(i)
