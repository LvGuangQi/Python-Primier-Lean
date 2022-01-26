li = [11,22,33,44,55,66,77,88,99,90]
dic = {}
n = []
m = []
for i in li:
    if i > 66:
        m.append(i)
    if i<66:
        n.append(i)
dic.update(k1 = m, k2 = n)
print(dic)