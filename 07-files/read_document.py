
file = open('document.txt')

lines = file.readlines()

for line in lines:
    line = line.strip()
    if(len(line) > 0):
        print(line)