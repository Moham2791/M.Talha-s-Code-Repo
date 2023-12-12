array = [2, 1, 90, 5]

# basic sorting
# for i in range(len(array)):

#  for j in range(0, i+1):

#   if array[i] < array[j]:
#
#         array[i], array[j] = array[j], array[i]

# print(array)

# selection sorting

empty = []

for i in range(len(array)):
    ele = min(array)
    index = array.index(min(array))

    del array[index]
    empty.append(ele)

print(empty)


# def selection_sort(array):
#sorted_array = []
# Initializing the second array with spaces in it
#  for i in range(len(array)):
#    sorted_array.append(" ")
# for i in range(len(array)):
# Take minimum element in the array
#  ele = min(array)
# taking the index of the minimum element
#   index = array.index(min(array))
# Removing the minimum element in the array
#   del array[index]
# Adding the minimum element to second array
#   sorted_array[i] = ele
#  print("Elements After Sorting")
#  for val in sorted_array:
#  print(val, end=" ")


#print("Enter elements into array")
#array = [int(n) for n in input().split()]
# selection_sort(array)
