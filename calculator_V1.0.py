import operator
from time import sleep, time

input_ok = True
operator = ["+", "-", "*", "/", "%", "//", "<", ">" ]
def add(x, y):
    return x + y

def substract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def remainder_of_division(x, y):
    return x % y

def divide_wo_remainder(x, y):
    return x // y

def is_bigger(x, y):
    return x > y

def is_smaller(x, y):
    return x < y



while input_ok == True:
    operation = input("Enter the operation You'd like to do(+, -, *, /, %, //, <, > ): ")

    if operation not in operator:
        print("You must choose from predefinied operations!!!")
        continue
    else:
        try:
            num_1 = input("Enter first number: ")
            num_1 = float(num_1)

            num_2 = input("Enter second number: ")
            num_2 = float(num_2)
        except ValueError:
            print("You Have to enter a number!!!")
            continue
        
        if operation == "+":
            placeholder = add(num_1, num_2)
            print(f"The result is {placeholder}")     
        elif operation == "-":
            placeholder = substract(num_1, num_2)
            print(f"The result is {placeholder}")      
        elif operation == "*":
            placeholder = multiply(num_1, num_2)
            print(f"The result is {placeholder}") 
        elif operation == "/":
            placeholder = divide(num_1, num_2)
            print(f"The result is {placeholder}") 
        elif operation == "%":
            placeholder = remainder_of_division(num_1, num_2)
            print(f"The result is {placeholder}") 
        elif operation == "//":
            placeholder = divide_wo_remainder(num_1, num_2)
            print(f"The result is {placeholder}") 
        elif operation == ">":
            placeholder = is_bigger(num_1, num_2)
            print(f"The result is {placeholder}") 
        elif operation == "<":
            placeholder = is_smaller(num_1, num_2)
            print(f"The result is {placeholder}")
    
    cnt = input("If you wish to continue enter Y/y, otherwise N/n: ").lower()
    if cnt == "n":
        print("Thanks for using my calculator")
        sleep(3)
        break
    else:
        print("You may continue wit ur meth :o")
        continue