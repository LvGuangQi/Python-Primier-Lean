n=input('输入:')#输入字符串
m=n[ ::-1]#倒序输出
if m==n:#判断是否相等4
    print("{}是回文数".format(n))#format方法输出
else:
    print("{}不是回文数".format(n))#format方法输出
