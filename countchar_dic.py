# Count the number of each chars in a string. Use Dictionary. 
# Print the chars and its num of occurrence in the same order as it appears in the string
#we attack at dawn
string = "we attack at dawn"
char_count = {}
# iterate the string 
for char in string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
# this for loop is use for print purpose
for char in string:
    if char in char_count:
        print(char,":",char_count[char])
        # repeated char is not print here only it take the count of repeated words so 
        # here we use 'del'
        del char_count[char]
#output -  w2e1a4...

'''
OUTPUT:

w : 2
e : 1
  : 3
a : 4
t : 3
c : 1
k : 1
d : 1
n : 1

'''