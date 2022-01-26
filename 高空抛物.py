sum = 100
for i in range(1, 10):
    print('第', i, '次反弹', 100 * (2 ** -i))
    sum += 100 * (2 ** -i) * 2
print(sum)