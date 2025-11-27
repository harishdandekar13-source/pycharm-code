num1=int(input("Enter the first number:"))
num2=int(input("enter the second number:"))
operator=input("enter the operator(+,-,*,/):")
if operator=='+':
    print(f"{num1}+{num2}=",num1+num2)
elif operator=='-':
    print(f"{num1}-{num2}=",num1-num2)
elif operator=='*':
    print(f"{num1}*{num2}=",num1*num2)
elif operator=='/':
    print(f"{num1}//{num2}=",num1/num2)
else:
    print("invalid operator")