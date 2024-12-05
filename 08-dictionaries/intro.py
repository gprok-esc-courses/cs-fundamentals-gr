student_grades = {}

# student_grades = {'john': 45, 'ann': 47, 'peter': 67, 
#                   'mike': 60, 'mary': 48}

student_grades['john'] = 45
student_grades['ann'] = 47
student_grades['peter'] = 67
student_grades['mike'] = 60
student_grades['mary'] = 48

# for k in student_grades:
#     print(k, student_grades[k])

name = input("Student name: ")
if name in student_grades:
    print(student_grades[name])
else:
    print("Student not found")