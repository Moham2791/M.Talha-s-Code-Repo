list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
j = 1
for i in range(len(list1)):
    list2.insert(j, list1[i])
    j += 2


print(list2)
