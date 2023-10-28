def add(n1,n2):
    return n1 + n2

def subrtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

operations = {
"+" : add,
"-" : subrtract,
"*" : multiply,
"/" : divide

}
def calculation():
    should_continue = True
    first_number = float(input("what's the first number?"))
    for symbol in operations:
        print(symbol)

    while should_continue:
        pick_operation = input("pick an operation: ")
        next_number = float(input("what's the next number?"))


        calculate_function = operations[pick_operation]
        answer = calculate_function(first_number,next_number)
        print(f"{first_number} {pick_operation}{next_number}={answer}")



        if input("Type'y' to continue calculating with , or type 'n' to start  a new calculate:") == "y":
            first_number = answer
        else:
            first_number =False
            calculation()

calculation()