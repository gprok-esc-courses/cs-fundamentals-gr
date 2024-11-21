
word = input("Give a word: ")

print(word)
# print word with first letter, dashes, and last letter
# Example: object will be presented as o----t
secret = word[0]
for i in range(1, len(word)-1):
    secret += '-'
secret += word[-1]
print(secret)

secret2 = word[0] + '-' * (len(word) - 2) + word[-1]
print(secret2)
