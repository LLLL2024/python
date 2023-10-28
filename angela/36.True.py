name1 = input("your name:  ")
name2 = input ("her name:  ")

combing_string = name1 + name2
lower_combing_string = combing_string.lower()

T = lower_combing_string.count("t")
R = lower_combing_string.count("r")
U = lower_combing_string.count("u")
E = lower_combing_string.count("e")
L = lower_combing_string.count("l")
O = lower_combing_string.count("o")
V = lower_combing_string.count("v")

TRUE = T + R + U + E
print(int(TRUE))

LOVE = L + O + V + E
print(int(LOVE))

Love_Score = int(str(TRUE)  + str(LOVE))
print(Love_Score)

if Love_Score < 10 or Love_Score > 90:
     print(f"You score is {Love_Score},you go together like coke and mentos.")

elif 40 <= Love_Score <= 50:
    print(f"Your socre is {Love_Score},you are alright together.")

else:
    print(f"you socre is {Love_Score}")