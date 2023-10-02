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

#Problem #3
Get a input. Create a sequence of numbers from that input using the above alg.
Find the largest number in the sequence. 
'''
# Get the input number from the user
input_number = int(input("Enter the  input number: "))
sequence = []
#check the number is not equal to one
while input_number != 1:
    # append the current number to the sequence
    sequence.append(input_number) 
    #check thenumber is odd or even 
    if input_number % 2 == 0:
        input_number = input_number // 2
    else:
        input_number = 3 * input_number + 1
    # Append the last iterative answer (it is alway 1)
    sequence.append(input_number)  


# Find the largest number in the sequence
largest_number = max(sequence)
#print the sequence
print(f"the sequence for {input_number} is: {sequence}")
print(f"the largest number in the sequence is: {largest_number}")

'''
output:

Enter the  input number: 10
the sequence for 1 is: [10, 5, 5, 16, 16, 8, 8, 4, 4, 2, 2, 1]
the largest number in the sequence is: 16
'''