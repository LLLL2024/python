def ints(i):
    i = 0
    a = True
    m = []

    while a == True:
        number = int(input("input a number\n"))
        n = []
        print(n)
        n.append(number)

        for number in n:
            i = number
            print(i)
            end = i % 2

            if end == 0:
                print(i)
                m.append(i)

        print(n)
        print(m)



