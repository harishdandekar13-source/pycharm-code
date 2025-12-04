def remove_duplicates(lst):
    unique = []
    for item in lst:
        if item not in unique:
             unique.append(item)
    return unique
a=[1,2,2,3,5,6,3,4,7]
print(remove_duplicates(a))


