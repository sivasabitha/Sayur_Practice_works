'''
Problem #1
Print the following pattern
1
212
32123
4321234
543212345
Get user input for how far to go (up to 0)
'''
#initialize the input
numbers = '1234567890'
#start for loop
for num in range(len(numbers)):
    #use slice function
    pattern = numbers[num:0:-1] + numbers[:num+1]
    #print the pattern
    print(pattern)

'''
output: 

1
212
32123
4321234
543212345
65432123456
7654321234567
876543212345678
98765432123456789
0987654321234567890
'''


