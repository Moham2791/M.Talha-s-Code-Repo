

from tkinter import E

print("enter")
user = input()

empty = []
newstring = ''

for i in range(len(user)):
    empty.append(user[i])

newvar = empty[::-1]

for j in range(len(newvar)):

    newstring += newvar[j]

if newstring == user:
    print("is a palindrome")
else:
    print("is not a palindrome")
