I = float(input("请输入当月利润，单位为万元："))
if I <= 10:
    bns = 10 * 0.1
elif 10 < I <= 20:
    bns = 10 * 0.1 + (I-10) * 0.075
elif 20 < I <= 40:
    bns = 10 * 0.1 + 10 * 0.075 + (I-20) * 0.05
elif 40 < I <= 60:
    bns = 10 * 0.1+ 10 * 0.075 + 20 * 0.05 + (I-40) * 0.03
elif 60 < I <= 100:
    bns = 10 * 0.1+ 10 * 0.075 + 20 * 0.05 + 20 * 0.03 + (I-60) * 0.015
elif I > 100:
    bns = 10 * 0.1 + 10 * 0.075 + 20 * 0.05 + 20 * 0.03 + 40 * 0.015 + (I-100) * 0.015
print(bns,'万元')