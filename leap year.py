print("please enter your current year")


year = int(input())


for i in range(1, 21):
    if year % 4 != 0:
        year += 1
    else:
        year += 4
        print(f"Leap year 20{year}")
