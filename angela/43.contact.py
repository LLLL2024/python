import random
name = input("name:").split(",")
names= len(name)

#extra_name = random.randint(0,names-1)
#people_who_will_pay = name[extra_name]
people_who_will_pay = random.choice(name)
print(people_who_will_pay + "  is going to be pay")