import random

correct = []
wrong = []

# Generate random word
word_list = [
    'object', 'oriented', 'inheritance', 'polymorphism',
    'usability', 'accessibility', 'microporcessor',
    'debugging', 'compiler', 'interpreter'
]

pos = random.randint(0, len(word_list)-1)
word = word_list[pos]
print(word)
secret = word[0] + '-' * (len(word) - 2) + word[-1]

# Loop 
while True:

    # Display secret
    print(secret)

    # Ask user for letter
    letter = input("Type one letter: ")

    # Update correct or wrong
    if letter in correct or letter in wrong:
        pass
    else:
        if letter in word:
            correct.append(letter)
        else:
            wrong.append(letter)

    # construct secret
    secret = word[0]
    for i in range(1, len(word)-1):
        if word[i] in correct:
            secret += word[i]
        else:
            secret += '-'
    secret += word[-1]

    # if secret == word FOUND and STOP
    if secret == word:
        print(secret)
        print("FOUND!")
        break

    # if len(wrong) is 6, HANGED and STOP
    if len(wrong) == 6:
        print("HANGED!")
        break