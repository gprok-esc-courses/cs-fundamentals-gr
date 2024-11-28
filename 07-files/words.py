
file = open('document.txt')

lines = file.readlines()

counter = 0
characters = 0

for line in lines:
    line = line.strip()
    if len(line) > 0:
        words = line.split()
        counter = counter + len(words)
        characters = characters + len(line)

print(counter)
print(characters)