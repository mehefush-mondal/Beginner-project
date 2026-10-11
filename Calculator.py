def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def multy(num1,num2):
    return num1*num2
def div(num1,num2):
    if num2 == 0:
        return"Cannot divide by zero"
    return num1/num2
def mod(num1,num2):
    if num2 == 0:
        return"Cannot divide by zero"
    return num1%num2
def sqre(num1,num2):
    return num1**num2

while True:
    try:
        num1=int(input("Enter 1st Number ="))
        op=input("Enter Operator '+', '-', '*', '/', '%', '**' =")
        num2=int(input("Enter 2nd Number ="))
    except ValueError:
        print("Enter a valid Number")
        continue

    if op == "+":
        result=add(num1,num2)
    elif op == "-":
        result=sub(num1,num2)
    elif op == "*":
        result=multy(num1,num2)
    elif op == "/":
        result=div(num1,num2)
    elif op == "%":
        result=mod(num1,num2)
    elif op == "**":
        result=sqre(num1,num2)
    else:
        result="Invalid Operstor Entered"

    print("Result =",result)

    while True:
        again = input("Do another calculation? (y/n): ").lower()
        if again == "n" or again == "y":
            break
        print("Please enter y or n.")

    if again == "n":
        break
