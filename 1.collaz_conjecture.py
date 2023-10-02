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
'''

# get the input number from the user
number = int(input("Enter the number: "))

# print the initial number
print(number)
#check the number is not equal to 1
while number != 1:
    # check if the number is even or odd
    if number % 2 == 0:
        number = number // 2
    else:
        number = 3 * number + 1
    # print the current number
    print(number)

'''
output:

Enter the number: 10
10
5
16
8
4
2
1
'''