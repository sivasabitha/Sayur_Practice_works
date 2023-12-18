'''
Problem #4
Input is an array of strings of an arithmetic expression. Calculate the value.
eg - input ["1", "2", "+", "5", "*"]
output =  15
explanation (1 + 2) * 5 = 15

input ["10", "2", "3", "+","-", "5", "*"]
output =  25
explanation (10 - ( 2 + 3)) * 5 = 25
Hint : Use the concept of stack. Push and pop. 
Parse the input list one element at a time. Convert to integer, push it to a stack. Whenever you see an
operator, pop two elements from the stack, apply the operation and push the result back.
'''

#create the function
def operator(input_list):
    #initialize the empty stack
    stack = []
    for input in input_list:
        #initialize the opertors
        operators = ['+', '-', '*', '/']
        #check the input is operator then pop the appened elements in the stack
        if input in operators:  
            b = int(stack.pop())
            a = int(stack.pop())
            #after the pop do the arithmetic operations
            if input == '+':
                result = a + b
            elif input == '-':
                result = a - b
            elif input == '*':
                result = a * b
            elif input == '/':
                if b == 0:
                    print("division by zero is not allowed")
                    break
                else:
                    result = a / b
            #append the result in the stack
            stack.append(str(result))
        #inut is number then push the numbers in the stack
        else:
            stack.append(input)
    #return the stack's 0 index(0th index is hold the answer)
    return stack[0]

#initialize the input_list  then call the function print the output
input_list = ["10", "2", "3", "+", "-", "5", "*"]
final_result = operator(input_list)
print(f"input: {input_list}")
print(f"output: {final_result}")

'''
output:

input: ['10', '2', '3', '+', '-', '5', '*']
output: 25
'''

