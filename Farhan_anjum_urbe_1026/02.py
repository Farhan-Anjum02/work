name = input("Enter a string: ")
print("Full Name: ", name)
a=[]
for i in name:
    a.append(ord(i))
print("ASCII values: ",a)