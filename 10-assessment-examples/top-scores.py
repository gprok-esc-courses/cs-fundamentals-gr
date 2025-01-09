scores = {
    "a": 0,
    "b": 7,
    "c": 4,
    "d": 2,
    "e": 1,
    "f": 4
}
# Find top 3
ordered_score = list(sorted(scores.items(), 
             key=lambda item: item[1],
             reverse=True))
for i in range(3):
    print(ordered_score[i])
