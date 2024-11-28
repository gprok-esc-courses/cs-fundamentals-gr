
try:
    file = open('no_file.txt')
except FileNotFoundError:
    print('File not found')