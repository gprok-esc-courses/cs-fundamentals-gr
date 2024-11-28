
file = open('userdata.txt', 'a')

sentence = ''

while sentence != 'END':
    sentence = input("Type sentence, END to stop: ")
    if sentence != 'END':
        file.write(sentence + '\n')