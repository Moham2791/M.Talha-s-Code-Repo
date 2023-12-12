sum_ = 0
product_ = 1

n = int(input("enter the number  : "))


answer = input(" product or sum ? ")

for i in range(1, n):

    if answer == "sum ":
        sum_ += i
print(sum_)

# if answer == "product":
#         product_*=i

# print(product_)
