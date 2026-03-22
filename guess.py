import random
playing=True
number=str(random.randint(0,9))
print("Guess the number between 0 and 9")
while playing:
    guess=input("Enter your guess: ")

    if number==guess:
        print("Congratulations! You guessed the number.")
        print("The number was:", number)
        break
    else:
        print("Wrong guess. Try again.")