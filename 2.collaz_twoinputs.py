'''
Problem #1
Write a program for Collatz_conjecture.
Collatz_conjecture means -  start with the input number. 
For even number , divide by 2 (n/2)
For odd number - 3n + 1
apply the above for the result number until the answer is 1.

Eg, input is 8
8, 4,2, 1
input is 9
9,28,14,7,22,11,34,17,52,26,13,40,20,10,5,16,8,4,2,1

Problem #2
Same as above.
Input two numbers.
Print which number has less steps to reach 1.
'''
# Get the two input numbers from the user
input_number1 = int(input("Enter the first number: "))
input_number2 = int(input("Enter the second number: "))
#after looping process the input numbers are over write so we use this step
number1 = input_number1
number2 = input_number2
count1 = 0
count2 = 0

# Check that the input numbers are not equal to 1
while number1 != 1:
    # Check if the number1 is odd or even
    if number1 % 2 == 0:
        number1 = number1 // 2
    else:
        number1 = 3 * number1 + 1
    # Increment the count
    count1 += 1

# Reset the number2 to its original value
number2 = input_number2

# Check that the input numbers are not equal to 1
while number2 != 1:
    # Check if the number2 is odd or even
    if number2 % 2 == 0:
        number2 = number2 // 2
    else:
        number2 = 3 * number2 + 1
    # Increment the count
    count2 += 1
#check the count1 is less than count 2
if count1 < count2:
    print(f"{input_number1} reaches 1 in ({count1} steps)")
#check the count2 is less than count 1
elif count2 < count1:
    print(f"{input_number2} reaches 1 in  ({count2} steps)")
else:
    print(f"Both numbers reach 1 in the same number of ({count1} steps)")


'''
output:

Enter the first number: 10
Enter the second number: 8
8 reaches 1 in  (3 steps)
'''

