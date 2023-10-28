years = int(input("years:"))
if years % 4  == 0:
    if years % 100 == 0:
        if years % 400 == 0:
            print(f"so the year {years} is  leap")
        else:
            print(f"so the year {years} is not leap")
    else:
        print(f"so the year {years} is  leap")
else:
    print(f"so the year {years} is not leap")