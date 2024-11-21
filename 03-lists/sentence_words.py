
# Ask user to give a sentence,
# then find how many words are in the sentence

sentence = input("Write a sentence: ")

counter = 0
flag = 'space'

for i in range(len(sentence)):
    if sentence[i] == ' ':
        flag = 'space'
    else:
        if flag == 'space':
            counter += 1
            flag = 'letter'
    
print(counter)

words = sentence.split()
print(words)
print(len(words))