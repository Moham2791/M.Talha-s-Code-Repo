

print("enter the number")
user = int(input())
nums = list(range(1, 100))


if user in nums:
    print(f"{user} exists")
else:
    print("Doesnt exist")
