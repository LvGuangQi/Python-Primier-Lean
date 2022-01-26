def d(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return (n-1)*(d(n-1) + d(n-2))

n=int(input("信封个数:"))
print(d(n))