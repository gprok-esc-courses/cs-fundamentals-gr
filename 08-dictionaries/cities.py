
file = open('cities.csv')
lines = file.readlines()

states = {}

for i in range(1, len(lines)):
    line = lines[i]
    elements = line.split(',')

    if len(elements) > 1:
        state = elements[-1].strip()
        city = elements[-2].strip()
        city = city[1:-2]

        if state in states:
            states[state].append(city)
        else:
            states[state] = [city]

s = input("State: ")
if s in states:
    print(states[s])
else:
    print("State", s, "not found")
