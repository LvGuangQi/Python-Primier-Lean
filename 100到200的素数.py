sum=0
for i in range(101,201):
    for j in range(2,i-1):
        if i%j==0:
            break
    else:
        print(i)
        sum+=1
print(sum)