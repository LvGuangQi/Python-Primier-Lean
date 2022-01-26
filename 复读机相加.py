a=input('被加数字:')
n=int(input( '加几次: '))
b=0
for i in range(n):
    b+=int(a)
    a+=a[0]
print('结果是: ', b)