import random

secret_number = random.randint(1, 100)
isGuessed = False



while not isGuessed:
    try:
        number = int(input("Enter a number between 1 to 100: "))

        if number < 1 or number > 100:
            print("Please enter a number within the range 1 to 100.")
            continue
            
        if number == secret_number:
            print("Correct! You guessed the number.")
            isGuessed = True
        elif number < secret_number:
            print("Too Low.")
        else:
            print("Too High.")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

