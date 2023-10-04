'''
Problem 2:
Write a program to calculate avg marks of your class, in CS subject in the last 3 exams.
'''
# create function to calculate the average marks for the class
def calculate_class_avg():
    # initialize the total marks for the class
    total_class_marks = 0
    
    # get the input from user for the number of students in the class
    num_students = int(input("enter the number of students in the class: "))
    
    # use forloop to  get input marks for all student for the last 3 exams 
    for student in range(num_students):
        #initialize student mark is 0
        student_marks = 0
        for exam in range(3):
            # get the marks for all exam from the user for all students
            exam_marks = float(input(f"Enter marks for CS exam {exam+1} for student {student+1}: "))
            # add the total marks to the students
            student_marks += exam_marks 
         # Add the students total to the class total
        total_class_marks += student_marks 
    
    # calculate the average marks for the class
    avg_class_marks = total_class_marks / (num_students * 3)
    #return the avrge mark
    return avg_class_marks

# main code
#call the function
avg_cs_class = calculate_class_avg()
# print the result
print(f"The average marks in CS for the class in the last 3 exams is: {avg_cs_class}")


'''
output:

enter the number of students in the class: 3
Enter marks for CS exam 1 for student 1: 87
Enter marks for CS exam 2 for student 1: 98
Enter marks for CS exam 3 for student 1: 99
Enter marks for CS exam 1 for student 2: 76
Enter marks for CS exam 2 for student 2: 89
Enter marks for CS exam 3 for student 2: 79
Enter marks for CS exam 1 for student 3: 87
Enter marks for CS exam 2 for student 3: 90
Enter marks for CS exam 3 for student 3: 98
The average marks in CS for the class in the last 3 exams is: 89.22222222222223
'''