data = [1, 2, 3, 4, 5, 6]

k = input()
i = 0
count = 0
for i in range(len(data)):
    count += 1
    while count != k:
        data[i].pop()
        data[i].append()
print(data)
