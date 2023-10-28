numbers = [8, 10, 14, 17, 20, 22]
numbers.append(20)
print(numbers)

numbers = [8, 10, 14, 17, 20, 22]
numbers.insert(1,21)
print(numbers)

numbers = [8, 10, 14, 17, 20, 22]
numbers.remove(8)
print(numbers)

numbers = [8, 10, 14, 17, 20, 22]
numbers.clear()
print(numbers)

numbers = [8, 10, 14, 17, 20, 22]
numbers.pop()
print(numbers)

numbers = [8, 10, 14, 17, 20, 22]
print(numbers.index(8))

numbers = [8, 10, 14, 17, 20, 22]
print(50 in numbers)

numbers = [8, 10, 14, 17, 14, 22]
print(numbers.count(14))

numbers = [8, 10, 24,17,20, 22]
numbers.sort()
numbers.reverse()
print(numbers)

numbers = [8, 10, 14, 17, 20, 22]
numbers_2 = numbers.copy()
numbers.append(25)
print(numbers_2)

numbers = [3, 6,6,7,9 ,13, 15, 19, 22]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

