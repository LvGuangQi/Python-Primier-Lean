# 角谷定理的实现，返回运算次数
def jiaogu(step, num):
#  递归出口
#  当输入数据num = 1时，直接输出num和默认运算次数0
    if num==1:
        return step
    # 当输入偶数时，num/2，step+1，递归直至num = 1，输出每次除2所得数据和次数
    elif num%2==0:
        print(int(num/2), end=" ")  # 输出运算中间数据
        step += 1
        return jiaogu(step, num/2) # 递归体定于，返回运算次数
    # 输入数据为奇数时，num*3 + 1 step++  递归直至num = 1，输出数据和次数
    else:
        print(num * 3 + 1, end=" ")
        step +=1
        return jiaogu(step, num*3+1) # 递归体，返回运算次数
def main():
    step = 0  # step=0表示当输入的数字num=1时，直接输出1，不需要进行运算
    num = int(input('请输入一个自然数:'))
    print(num, end=" ")
    print("\nstep = %d\n" % (jiaogu(step, num)))
if __name__ == '__main__':
    main()