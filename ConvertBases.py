
starting = [1, 2, 3, 4, 5, 6, 7]

ans = []


print("Please enter a base target")

target = int(input())


for i in range(len(starting)-1):

    if len(starting) > target:

        if len(ans) < target:
            ans.append(starting[i])

    elif len(starting) < target:
        starting.append(0)


print(f"The starting {starting} has been converted to target :{target}")


ans.sort()
print(ans)
