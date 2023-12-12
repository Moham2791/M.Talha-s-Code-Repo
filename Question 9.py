target = 25
tries = 0
prev = None
while True:
    guess = int(input("Please Guess the number : "))
    if prev != guess:
        tries += 1
        prev = guess

    if guess < target:
        print(f'The number is too small')

    elif guess > target:
        print(f"The number is too large.")

    else:
        print(f"Correct ! Tries taken :{tries} ")
        break

# by the end return the number of tries it took the person to get the target
