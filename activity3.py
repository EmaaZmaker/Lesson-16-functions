def addition (P,Q):
    return P+Q
def subtraction (P,Q):
    return P-Q
def multiplication (P,Q):
    return P*Q
def divide (P,Q):
    return P/Q
num1=int(input("enter a number"))
num2=int(input("enter a number"))
print("please press")
print("a.addition")
print("b.subtraction")
print("c.multiplication")
print("d.division")
choice=input("enter your choice")
if choice=="a":
    print("the addition of numbers is",addition(num1,num2))
elif choice=="b":
    print("the subtraction of numbers is",subtraction(num1,num2))
elif choice=="c":
    print("the multiplication of numbers is",multiplication(num1,num2))
elif choice=="d":
    print("the division of numbers is",divide(num1,num2))
else:
    print("please provide a valid input")
