newlist = list(range(1, 9))

print(newlist)

primelist = []


num = 1

for i in newlist:
    if i % num == 0 and i != num:
        continue
    elif i % num == 0 and i == num:
        primelist.append(num)
        num += 1
        print(primelist)

# for every number form 1 to n
# if number is prime : add to list

# function is_prime(x)
   # for i in range(2,x)
   #    if x % i == 0:
   #       return false
   # return true
