'''
Problem 1:
Write a program to calculate your avg marks in CS subject in the last 3 exams.
'''
# write function to calculate the average marks
def calculate_avg_marks():
    # initialize total marks as 0
    total_marks = 0
    #use forloop to get the marks from user and add the 3 marks
    for mark in range(3):
        # get the marks for each exam from user
        exam_marks = float(input(f"Enter marks for CS exam {mark+1}: "))
        # add the total marks
        total_marks += exam_marks 
    # calculate the average marks
    average_marks = total_marks / 3
    return average_marks

# main code
#call the function 
avg_cs_marks = calculate_avg_marks()

# print the result
print(f"average marks in CS for the last 3 exams is: {avg_cs_marks}")

'''
output:

Enter marks for CS exam 1: 35
Enter marks for CS exam 2: 78
Enter marks for CS exam 3: 98
average marks in CS for the last 3 exams is: 70.33333333333333
'''
