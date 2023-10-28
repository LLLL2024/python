student_score = input("Input student height: ").split()
hightest_socre  = 0
for score in student_score:
    scores = int(score)
    if scores > hightest_socre:
         hightest_socre = scores
print(f"this hightest is {hightest_socre}")