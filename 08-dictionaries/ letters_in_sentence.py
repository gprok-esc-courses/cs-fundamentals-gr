
sentence = input("Type a sentence: ")
sentence = sentence.lower()

letters = {}

for ch in sentence:
    if ch != ' ':
        if ch in letters:
            letters[ch] += 1
            # letters[ch] = letters[ch] + 1
        else:
            letters[ch] = 1

for key in letters:
    print(key, letters[key])