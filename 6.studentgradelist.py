'''
Problem #3
you have a list of student names. you have one list each for their marks in CS, Math and English. 
hard code the values. no need to get it as input
Pass mark is 50.
Grade A is, mark 90 or above
Grade B , 80 or above
Fail is < 50
Print the name of the students who got A in all subjects or atleast one A and the rest B.
Try to use only one if statement.
'''
#initialize the  hardcoded  input for student names
student_names = ["ram", "raj", "jai", "rani", "ravi"]

#initialize the hardcoded lists of marks in CS, Math, and English
marks_in_CS = [90, 96, 88, 92, 98]
marks_in_Math = [88, 92, 51, 99, 93]
marks_in_English = [91, 99, 80, 82, 95]

# iterate through the students
for student in range(len(student_names)):
    name = student_names[student]
    cs_mark = marks_in_CS[student]
    math_mark = marks_in_Math[student]
    english_mark = marks_in_English[student]

    # check if the student got an A grade in all subjects or at least one A and the rest B
    if cs_mark >= 90 and math_mark >= 90 and english_mark >= 90:
        print(f"{name} got an A in all subjects.")
    elif (cs_mark >= 90 or math_mark >= 90 or english_mark >= 90) and (cs_mark >= 80 and math_mark >= 80 and english_mark >= 80):
        print(f"{name} got at least one A and the rest B.")

'''
output:

ram got at least one A and the rest B.
raj got an A in all subjects.
ravi got an A in all subjects.
'''
