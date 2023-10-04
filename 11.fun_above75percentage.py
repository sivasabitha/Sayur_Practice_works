'''
Problem 3:
Write a program to calculate avg marks for each student and no of students whose avg is above 75%
 in CS subject in the last 3 exams.
'''
# write a function to calculate the average marks for a single student
def calculate_student_avg():
    # initialize the total marks for the student is 0
    total_student_marks = 0
    
    # use forloop to get input marks for the last 3 exams for the student
    for exam in range(3):
        # get the marks for each exam from the user for the student
        exam_marks = float(input(f"Enter marks for CS exam {exam+1}: "))
        # add the total marks to the students 
        total_student_marks += exam_marks  
    
    # calculate the average marks for the student
    avg_student_marks = total_student_marks / 3
    
    return avg_student_marks

# main code
num_of_students = int(input("Enter the number of students: "))
# initialize a count for students with averages above 75% is 0
above_75_count = 0 
# this for loop is used to get each students percentage , inside the loop we using function call
for student in range(num_of_students):
    print(f"Student {student+1}:")
    avg_cs_student = calculate_student_avg()
    print(f"Average marks for student {student+1} in CS: {avg_cs_student}")
    
    # check if the students average is above 75% it is true then add the count of students here
    if avg_cs_student > 75:
        above_75_count += 1

# print the number of students with averages above 75%
print(f"The number of students with averages above 75%: {above_75_count}")

'''
output:

Enter the number of students: 2
Student 1:
Enter marks for CS exam 1: 87
Enter marks for CS exam 2: 98
Enter marks for CS exam 3: 90
Average marks for student 1 in CS: 91.66666666666667
Student 2:
Enter marks for CS exam 1: 98
Enter marks for CS exam 2: 56
Enter marks for CS exam 3: 45
Average marks for student 2 in CS: 66.33333333333333
The number of students with averages above 75%: 1
'''
