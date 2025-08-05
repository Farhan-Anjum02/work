# work
##  Problem Statement 01

Count and display the number of vowels and consonants in your name.


##  Technologies Used

- **Python 3**
- **Spyder IDE** (from Anaconda)


##  How to Run the Code in Spyder

1. **Open Spyder** (via Anaconda Navigator or Start Menu).
2. Create a **new Python file**, e.g., '01.py'.
3. Paste the following code:

   name = input("Enter a string: ")
   print("Full Name: ", name)
   vowels = 0
   consonants = 0

   for i in name:
       if i in 'aeiouAEIOU':
           vowels += 1
       elif (i >= 'A' and i <= 'Z') or (i >= 'a' and i <= 'z'):
           consonants += 1

   print("vowels:", vowels)
   print("consonants:", consonants)
   
4.Save the file.
5.Click the green "Run" button.


##  Input
Enter a string: Farhan Anjum Urbe


##  Output
Full Name:  Farhan Anjum Urbe
vowels: 6
consonants: 9



##  Problem Statement 02

Display the ASCII value of each character.



##  Technologies Used

- **Python 3**
- **Spyder IDE** 



##  How to Run the Code in Spyder

1. Open **Spyder**.
2. Create a new file, e.g., '02.py'.
3. Paste the following code into the file:

   
   name = input("Enter a string: ")
   print("Full Name: ", name)
   a = []
   for i in name:
       a.append(ord(i))
   print("ASCII values: ", a)

4.Save the file.
5.Click the green "Run" button.


##  Input
Enter a string: Farhan Anjum Urbe


##  Output
Full Name:  Farhan Anjum Urbe
ASCII values: [70,97,114,104,97,110,32,65,110,106,117,109,32,85,114,98,101]



## 📝 Problem Statement 03

Create a reversed version of your name.


## Technologies Used

- **Python 3**
- **Spyder IDE** 


##  How to Run the Code in Spyder

1. Open **Spyder**.
2. Create a new file, e.g., '03.py'.
3. Paste the following code into the file:

   name = input("Enter your name: ")
   print("Full Name: ", name)
   reversed_name = name[::-1]
   print("Reversed Name: ", reversed_name)

4.Save the file.
5.Click the green "Run" button.

#Input
Enter your name: Farhan Anjum Urbe

#Output
Full Name:  Farhan Anjum Urbe
Reversed Name:  ebrU mujnA nahraF


## 📝 Problem Statement 04

Check if your name is a palindrome.



##  Technologies Used

- **Python 3**
- **Spyder IDE** (Anaconda)


##  How to Run the Code in Spyder

1. Open **Spyder**.
2. Create a new file, for example: '04.py'.
3. Paste the following code:

   str = input("Enter full name: ")
   str1 = str[::-1]
   print("Is Palindrome: ", str1 == str)
4.Save the file.
5.Click the green "Run" button.

#Input
Enter your name: Farhan Anjum Urbe

#Output
Is Palindrome:  False


# Unique Letters Sorted Alphabetically

## 📝 Problem Statement 05

Store each unique letter of your name in a Python list and sort it alphabetically.


##  Technologies Used

- **Python 3**
- **Spyder IDE** 



##  How to Run the Code in Spyder

1. Open **Spyder**.
2. Create a new Python file, e.g., '05.py'.
3. Paste the following code:

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
   a.sort()  # Sort the list alphabetically
   print("Unique letters:", a)

4.Save the file.
5.Click the green "Run" button.

#Input
Enter your name: Farhan Anjum Urbe

#Output
Unique letters: ['A', 'F', 'N', 'R', 'U', 'a', 'b', 'e', 'h', 'j', 'm', 'n', 'r', 'u']



