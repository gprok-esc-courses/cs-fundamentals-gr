from random import randint

secret = randint(1, 100)
print(secret)

guess = 0
counter = 0

while guess != secret:
    guess = int(input("Guess: "))
    counter = counter + 1
    if guess > secret:
        print("Go down")
    elif guess < secret:
        print("Go up")
    else: 
        print("Found! in " + str(counter) + " guesses")