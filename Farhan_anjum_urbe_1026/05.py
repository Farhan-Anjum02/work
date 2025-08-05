str = input("Full Name: ")
a = []
for i in str:
    if (i >= 'A' and i <= 'Z') or (i >= 'a' and i <= 'z'):
        count = 0
        for j in range(len(a)):
            if a[j] == i:
                count += 1
                break
        if count == 0:
            a.append(i)
print("Unique letters:", a)
