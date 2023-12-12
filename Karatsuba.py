num1 = [1, 2, 3, 4, 5]
num2 = [3, 4, 5, 6, 7]

add = []
sub = []
multi = []
# addition
for i in range(len(num1)):
    for j in range(len(num2)):

        if i == j:
            add.append(num1[i]+num2[j])
            sub.append(abs(num1[i]-num2[j]))
            multi.append(num1[i]*num2[j])


print(f"This is sum of two lists {add}")
print(f"This is difference of two lists {sub}")

print(f"This product of two lists {multi}")
