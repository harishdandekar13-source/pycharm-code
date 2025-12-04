def sum_from_1_to_n(n):
    add=0
    for i in range(1,n+1):
        add+=i
    print(add)
n=int(input("Enter the number:"))
print("Sum of n natural number",sum_from_1_to_n(n))
