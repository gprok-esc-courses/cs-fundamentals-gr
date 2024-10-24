start = input("Give start: ")
start = int(start)
end = input("Give end: ")
end = int(end)

if start <= end:
    for i in range(start, end+1):
        print(i)
else:
    for i in range(start, end-1, -1):
        print(i)