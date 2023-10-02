'''
Problem #1
Generate the following output using for loop. Go until g.
a
aba
abacaba
abacabadabacaba
abacabadabacabaeabacabadabacaba

look at the output and find the pattern. Hint - add next letter in the alphabet in each row
'''

# Define the alphabet
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# Initialize the result string as 'a'
result = 'a'
print(result)

# Iterate through the alphabet until 'g' use slice function 
for letter in alphabet[1:7]:  
    result += letter + result

    # Print the current result
    print(result)

'''
output:

a
aba
abacaba
abacabadabacaba
abacabadabacabaeabacabadabacaba
abacabadabacabaeabacabadabacabafabacabadabacabaeabacabadabacaba
abacabadabacabaeabacabadabacabafabacabadabacabaeabacabadabacabagabacabadabacabaeabacabadabacabafabacabadabacabaeabacabadabacaba 
'''

