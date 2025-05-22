#Basic calculator in python
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
print("welcome to the calculator")
print("choose the operation")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")
operation=input("enter your choice(1/2/3/4):")
if operation in['1','2','3','4']:
    try:
        num1=float(input("enter the first number:"))
        num2=float(input("enter the second number:"))
    except ValueError:
        print("invalid input")
    else:
        if operation=='1':
            print("result:",add(num1,num2))
        elif operation=='2':
            print("result:",subtract(num1,num2))
        elif operation=='3':
            print("result:",multiply(num1,num2))
        elif operation=='4':
            print("result:",divide(num1,num2))
        else:
            print("invalid choice")