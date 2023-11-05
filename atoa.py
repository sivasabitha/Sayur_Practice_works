'''
Problem 1
In the input, find the first A and last A, print all the letters between these two A.
'''

#assign the name (string)
name="ababjutresca"
#assign the element to find the start char and end char, both are "a"
x=name.startswith('a')
y=name.endswith('a')
#check the start char and end char both are same
if x == y:
    #the both start char and end char are same then print the all characters between these two 'a
    for ch in (name[1:11]):
    #begin for
        print(ch)
    #end for
#else print the string isn't start and end with 'a'
else:
    print("input string is not start and end with 'a' ")


'''
output:

b
a
b
j
u
t
r
e
s
c
'''