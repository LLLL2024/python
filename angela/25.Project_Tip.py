print("welcome to the tip calculator")
bill = float(input("What was the total bill?$"))
tip = int((input("What percentage  tip would you like to give?")))
people = int(input("how many people to split the bill?"))

bill_with_tip= tip / 100 * bill + bill
everyone_bill = bill_with_tip / people
final_bill = round(everyone_bill,2)
final_bill = "{:.2f}".format(everyone_bill)
print("Each people should pay?  $",final_bill)