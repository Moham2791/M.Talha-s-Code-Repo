# Write a program that asks the user for a number n and prints the sum of the numbers 1 to n
print("Input a number")
n = int(input())
sum_ = 0
for i in range(1, n+1):
    sum_ += i

print(sum_)
