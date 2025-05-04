import random
print("Welcome to the Number Guessing Game!")

secret_number= random.randint(1,10)

attempts=0
while True:
    guess=input("guess a number between 1 and 10, or type q to quit: ")
    if guess.lower()=="quit":
        print("Thanks for playing!")
        break
    if not guess.isdigit():
        print("invalid input")
        continue
    guess=int(guess)
    attempts += 1

    if guess<secret_number:
        print("your guess is too low")
    elif guess>secret_number:
        print("your guess is too high")
    else:
        print(f"\nYOU GOT IT! You guessed it in {attempts} attempts.")
        break