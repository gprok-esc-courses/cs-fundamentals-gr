
s = "This is a string!"

c = input("Type a character: ")

counter = 0
lower_s = s.lower()
for i in range(len(s)):
    if lower_s[i] == c:
        counter += 1
print(c,"found",counter,"times")