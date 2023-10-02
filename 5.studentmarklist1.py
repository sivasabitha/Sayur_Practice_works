'''
Problem #2
you have a list of student names and another list with their marks in CS. 
hard code the values. no need to get it as input
Pass mark is 50.
Print a new list with all the students with pass marks along with their mark in the format name:mark.
Also print the number of students who failed.
'''
#initialize the hardcoded student names and marks
student_names = ["raj", "ram", "sai", "rani","sita"]
marks_in_CS = [65, 42, 58, 70,36]

# initialize lists for passed and failed students
passed_students = []
failed_students = []

# iterate through the students and their marks
for i in range(len(student_names)):
    name = student_names[i]
    mark = marks_in_CS[i]
    
    if mark >= 50:
        passed_students.append(f"{name}:{mark}")
    else:
        failed_students.append(f"{name}:{mark}")

# Print passed students and their  marks
print("Passed students:")
for pass_students in passed_students:
    print(pass_students)

# print the number of failed students 
print(f"Number of students who failed: {len(failed_students)}")
for fail_students in failed_students:
    print(fail_students)

'''
output:

Passed students:
raj:65
sai:58
rani:70
Number of students who failed: 2
ram:42
sita:36
'''