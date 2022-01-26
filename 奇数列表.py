import random
n = int(input("请输入一个整数："))
print("n = ", n)
my_list = []
for i in range(0, n) :
    num = random.randint(1, 100)
    while num % 2 == 0 :
        num = random.randint(1, 100)
    my_list.append(num)
print("排序前：", my_list)
# 排序
my_list.sort()
print("排序后：", my_list)