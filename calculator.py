print("===Sejal's Calculator===")

num1=float(input("enter your first number"))
operator=input("enter your operator")
num2=float(input("enter your second number +-*/"))
if operator=="+":
    result = num1+num2
elif operator=="-":
    result = num1-num2
elif operator=="*":
    result = num1*num2
elif operator=="/":
    result = num1/num2 
else:
    result ="wrong operator!"
print("Result:",result)       

