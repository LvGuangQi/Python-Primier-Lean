x=int(input("输入一个数:"))
guess=0
i=x #判断条件
while i!=0:
    guess+=x
    i-=1
print(str(x)+"*"+str(x)+"*"+"="+str(guess))