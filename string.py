s = input("Enter a string: ")

print("Concatenation:", s + " hiiiii")
print("Repetition:", s * 3)
print("Indexing: First character is", s[0])

print("Last character is", s[-1])   # corrected
print("Slicing: The first three characters are:", s[:3])

print("Is alphabet?", s.isalpha())
print("Is digit?", s.isdigit())
print("Is space?", s.isspace())

vowels = "aeiouAEIOU"
v = 0
c = 0

for char in s:
    if char.isalpha():  # count only letters
        if char in vowels:
            v += 1
        else:
            c += 1

print("Vowels:", v)
print("Consonants:", c)
