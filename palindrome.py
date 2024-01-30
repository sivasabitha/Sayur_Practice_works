'''
Problem #1
Input is a range of numbers as string. Print only the numbers that are palindromes and also the 
square of that number is also a palindrome.
eg. 121 is a palindrome and 121 * 121 = 14641 is also a palindrome, so you can print 121
131 is a palindrome, but 131*131 = 17161 is not a palindrome,so you can't print it.
eg input "10", "500"
Make sure to identify which steps need to be a function, how to avoid unnecessary parsing 
of numbers. Checking for palidrome or not, should be an efficient code.
'''
def find_palidrome(num):
    # use slice method  to reverse 
    if num==num[::-1]:
        # change the string to int
        num=int(num)
        # square the numbers
        square_of_palindrome=num*num
        # change int to string 
        square_of_palindrome=str(square_of_palindrome)
        # use slice method to reverse
        if square_of_palindrome==square_of_palindrome[::-1]:
            print("the square of the number is palindrome")
        else:
            print("the square of the number is not palindrome")
    else:
        print("your input number is not palindrome")
# main
# get the input is a range of numbers as string then cal the function
num=input("enter the number: ")
find_palidrome(num)

'''
OUTPUT:

enter the number: 121
the square of the number is palindrome

enter the number: 131
the square of the number is not palindrome

enter the number: 12
your input number is not palindrome

enter the number: 1
the square of the number is palindrome
'''