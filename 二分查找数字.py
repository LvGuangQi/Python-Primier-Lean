a =[]
def search(x, top, bot):  # 二分查找递归过程
    if top <= bot:
        mid = int((top + bot) / 2)  # 求中间数的位置
        if x == a[mid]:
            print("Yes") # 找到就输出
        elif x > a[mid]:
              # 判断在前半段还是后半段查找
            search(x,top,mid-1)
        else:
            search(x,mid+1,bot)
    else:
        print("NO")
def main():  # 主程序
    L, R = 0, 9
    print("输入10个从小到大顺序的数：")
    for i in range(10):
        y = int(input("请输入第%d个自然数：" % (i + 1)))
        a.append(y)
    x=int(input("需要查找的数:"))
    search(x, L, R)
if __name__ == '__main__':
    main()

