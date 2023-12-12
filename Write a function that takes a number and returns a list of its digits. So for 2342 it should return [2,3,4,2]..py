def convertToalistofDigits(num):

    print("enter a number")
    num = int(input())

    num = str(num)

    ans = []

    for i in range(len(num)):

        ans.append(int(num[i]))

    print(ans)

    print(type(ans))


convertToalistofDigits(0)
