l = '1234'
length = len(l)
def foo(length , lst=[]):
    if length == 0:
        return lst
    else:
        lst.append(l[length-1])
        return foo(length-1,lst)

ans =  foo(length)
print(ans)