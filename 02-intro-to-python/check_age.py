age = input("Give age: ")
age = int(age)
print(age)

if age <= 18:
    print("Young")
elif age >= 65:
    print("Old")
else:
    print("Middle age")