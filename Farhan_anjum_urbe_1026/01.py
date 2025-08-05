name = input("Enter a string: ")
print("Full Name: ",name)
vowels = 0
consonants = 0
for i in name:
    if i in 'aeiouAEIOU':
        vowels += 1
    elif (i >= 'A' and i <= 'Z') or (i >= 'a' and i <= 'z'):
        consonants += 1
print("vowels:", vowels)
print("consonants:", consonants)
