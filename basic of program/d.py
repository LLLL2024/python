correct_name = "python"
correct_password = "rules"
i = 0
n = True
while n == True:
    name = input("input user name\n")
    password = input("input user password\n")
    if correct_name == name and correct_password == password:
        print("welcome")
        n = False
    elif correct_name != name or correct_password != password:
        i += 1
        if  i == 5:
            print("Accessdenied")
            n = False
