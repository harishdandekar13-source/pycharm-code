num=int(input("Enter the number:"))
n=len(str(num))
sum=0
temp=num
while (temp>0):
    digit=temp%10
    sum+=digit**n
    temp//=10


if num==sum:
    print("it is an armstrong number")
else:
    print("it is a not an armstrong number")