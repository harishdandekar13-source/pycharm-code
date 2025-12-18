#sort arrange them in increasing order
#condition=what if a number is repeat
#so we creae a unique file
a=[1,2,33,5,6,47,33,47,8,5]
unique=[]
for item in a:
    if item not in unique:
        unique.append(item)


unique.sort()
print("The second largest number is:",unique[-2])