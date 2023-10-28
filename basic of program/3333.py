n = []
m =[]
a = True
def ins(i):
    end = i % 2
    if end == 0:
        print(i)
        m.append(i)

    print(n)
    print(m)
    return ins


while a == True:
    number = int(input("input a number\n"))
    n = []
    print(n)
    n.append(number)

    ins(number)