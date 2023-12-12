# Modify the previous program such that only the users Alice and Bob are greeted with their names.

print("Please Enter your Name")

name = input()

if name == "bob" or name == "alice":

    print(f"Welcome,{name}")
