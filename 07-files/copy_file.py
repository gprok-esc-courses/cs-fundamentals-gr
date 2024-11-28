
file = open('document.txt')
new_file = open('document_copy.txt', 'w')

lines = file.readlines()

for line in lines:
    new_file.write(line)