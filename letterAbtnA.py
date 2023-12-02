'''
Problem 1
In the input, find the first A and last A, print all the letters between these two A.
'''
#create a function for letters between A to A
def letterbtn_AtoA(input_string):
    #use find and rfind function to find letter
    first_A = input_string.find('A') 
    last_A = input_string.rfind('A')  
     #value is not found then find() function gives -1
     #first check 'A' is present or not
    if first_A == -1 and last_A == -1:
        print("'A' is not found in the string")
    #check the 'A' is present at 2 times('A' to 'A'),here first_a is true then it will be get index positin as 0
    elif first_A != last_A:
        letters_between_AtoA = input_string[first_A + 1:last_A]  
        print("letters between the first and last 'A':", letters_between_AtoA)
    #else only one 'a' is present 
    else:
        print("only one 'A' is present here")
        
# get the input string from user then call the function
input_text = input("enter the string: ")
letterbtn_AtoA(input_text)