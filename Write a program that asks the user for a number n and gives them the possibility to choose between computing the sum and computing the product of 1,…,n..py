# Write a program that asks the user for a number n and gives them the possibility to choose between computing the sum and computing the product of 1,…,n.

sum_ = 0
product_ = 1

print("Please enter a number")
n = int(input())

print("Do you want sum or product ?")

answer = input()

for i in range(1, n+1):

    if answer == 'sum':

        sum_ += i

    elif answer == 'product':
        product_ *= i

print(f"This is the sum of all the integers from 1 to n {sum_}")
print(f"This is the product of all the integers from 1 to n {product_}")
