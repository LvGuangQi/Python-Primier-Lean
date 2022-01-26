year=int(input('请输入第几年: '))
month=int(input('请输入是第几月:'))
day=int(input('请输入第几天:'))
Day_month=[31,28,31,30,31,30,31,31,30,31,30,31]
if (year % 4 == 0 and year %100 !=0) or (year %400 == 0):
    Day_month[1]=29
print("这天是今年的第{}天".format(sum(Day_month[0:month-1])+day))