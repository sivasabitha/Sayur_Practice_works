#adds two numbers
def addnumber(num1, num2) :
#takes two numbers 
    #add the numbers and return the result
    result=num1+num2
    return result 

#main code
#get input from users
num1=float(input("enter the number 1: "))
num2=float(input("enter the number 2: "))
result = addnumber(num1, num2)
print (f"the addition of two numbers is: {result}")

'''
output:

enter the number 1: 2
enter the number 2: 2
the addition of two numbers is: 4.0
'''