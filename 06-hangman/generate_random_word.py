import random

word_list = [
    'object', 'oriented', 'inheritance', 'polymorphism',
    'usability', 'accessibility', 'microporcessor',
    'debugging', 'compiler', 'interpreter'
]

print(len(word_list))

pos = random.randint(0, len(word_list)-1)
print(pos)
print(word_list[pos])