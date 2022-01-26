goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "奥特曼", "price": 998}
]
ass = int(input("请输入你的总资产:"))
dic={}
num =1
for i in goods:
    n = i["name"]
    dic.update({num : n})
    num +=1
print(dic)
zm = 0
while True:
    wan = int(input("请输入你想要的商品序号(按数字0结束;"))
    if wan == 0:
        break
    if wan > 4:
        print("请重新输入")
        continue
    v = dic.get(wan)
    print("你想要购买的是：", v)
    li = [0,1999, 10, 20, 998]
    print("它的价格为：%d"%li[wan])
    p = int(li[wan])
    zm = zm + p
if zm > ass:
    print("余额不足，请去充值")
else:
    print("购买成功！")