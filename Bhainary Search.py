v = list(range(1, 10))
lo = 0
high = len(v)-1
# iterative approach
print("Give a number for search")
t_point = int(input())

while high-lo > 1:
    mid = (high + lo)//2
    if v[mid] < t_point:
        lo = mid + 1
    else:
        high = mid

if v[lo] == t_point:
    print("Found At Index", lo)
elif v[high] == t_point:
    print("Found At Index", high)
else:
    print("Not Found")
# Hurn recursive approach
