x=int(input("请输入一个数:"))
guess=0
while guess**3<x:
    guess+=1
if guess**3!=x:
    print(str(x)+"不存在立方根")
else:
    print(str(x)+"存在立方根"+str(guess))