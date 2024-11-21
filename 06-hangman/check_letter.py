correct = []
wrong = []

word = "microprocessor"

while True:
    letter = input("Give one letter: ")

    if letter in correct or letter in wrong:
        pass
    else:
        if letter in word:
            correct.append(letter)
        else:
            wrong.append(letter)
    print(correct)
    print(wrong)