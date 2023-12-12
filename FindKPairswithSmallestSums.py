nums1 = [1, 7, 11]
nums2 = [2, 4, 6]
k = 3

empty = []
final = []

for i in range(len(nums1)):
    for j in range(len(nums2)):
        empty.append(nums1[i])
        empty.append(nums2[j])
        ans = final+empty
print(ans)
