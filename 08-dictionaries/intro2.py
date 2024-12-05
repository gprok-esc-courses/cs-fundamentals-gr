
student = {
    'id': 6785,
    'name': 'John Doe',
    'major': 'Computing',
    'grades': {'python': 65, 'math': 47, 'os': 48},
    'phone': '6785343456'
}

# print(student['grades']['math'])

info = input("What you want to learn: ")
if info == 'grades':
    course = input("Which course: ")
    if course in student['grades']:
        print(student['grades'][course])
    else:
        print(course, "not found")
elif info in student:
    print(student[info])
else: 
    print(info, "not available")