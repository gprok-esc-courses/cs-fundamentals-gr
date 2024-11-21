
word = 'polymorphism'
correct = ['s', 'y', 'p']

# Display m-ss-ss-ppi

secret = word[0]
for i in range(1, len(word)-1):
    if word[i] in correct:
        secret += word[i]
    else:
        secret += '-'
secret += word[-1]
print(secret)