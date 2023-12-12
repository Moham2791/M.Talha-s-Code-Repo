# Write a program that asks the user for a number n and gives them the possibility to choose between computing the sum and computing the product of 1,…,n.

print("Enter your input")

n = int(input())
count = 0
product = 0
for i in range(1, 13):
    product = n*i

    print(f"{n} X {i}={product}")
