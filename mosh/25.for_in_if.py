names= ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
names[0] = 'Joh'
print(names[2:])
print(names)

numbers = [12, 13, 15, 18, 19, 21]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)