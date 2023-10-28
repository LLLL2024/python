student_heights = input("Input a list of student heights \n").split()
heights_sum = 0
number_of_student= 0

for student in student_heights:
  number_of_student += 1
print(number_of_student)


for height in student_heights:
  heights_sum += int(height)
print(heights_sum)


average = heights_sum / number_of_student
number = round(average)
print(number)