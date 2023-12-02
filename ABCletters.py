'''
Problem 2:
  In the input, find the first A and last A, print all the letters between these two A. 
  If there is no A or 2nd A is not found, find the first B  and last B and print all the
    letters between these two B. 
  If there is no B or 2nd B is not found, find the first C and last C and print all the
    letters between these two C. 
'''
#create a function
def find_letters(input_string):
    #initialize the letters to find the first and last position
    first_A = input_string.find('A')
    last_A = input_string.rfind('A')
    first_B = input_string.find('B')
    last_B = input_string.rfind('B')
    first_C = input_string.find('C')
    last_C = input_string.rfind('C')
    #check 'A' to 'A' letters
    if first_A != -1 and last_A != -1 and first_A != last_A:
        letters_between = input_string[first_A + 1:last_A]
        print("letters between the first and last 'A':", letters_between)
    #check 'B' to 'B' letters
    elif first_B != -1 and last_B != -1 and first_B != last_B:
        letters_between = input_string[first_B + 1:last_B]
        print("letters between the first and last 'B':", letters_between)
    #check 'C' to 'C' letters
    elif first_C != -1 and last_C != -1 and first_C != last_C:
        letters_between = input_string[first_C + 1:last_C]
        print("letters between the first and last 'C':", letters_between)
    #else print letters ate not found
    else:
        print("letters 'A', 'B', or 'C'  is not found any letters in the string")

# get the input string from user then call the function
input_text = input("enter the string: ")
find_letters(input_text)
