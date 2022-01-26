year=int(input("Year:"))
month=int(input("Month:"))
if month==1 or month==3 or month==5 or month==7 or month==9 or month==10 or month==12:
    print("31")
elif month==2:
    if (year % 4 == 0 and year %100 !=0) or (year %400 == 0):
        print("29")
    else:
        print("28")
else:
    print("30")