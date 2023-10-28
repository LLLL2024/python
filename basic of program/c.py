def variable(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum
nums = [1,2,3,4]
print(variable(*nums))  #在list或tupe的前面加一个*号，把lsit或tupe变为可变参数引入进去