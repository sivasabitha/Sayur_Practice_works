'''
 Input is two strings. Find all the chars that are in both strings.
'''
#get the two strings from the user
name_one=input("Enter first string:")
name_two=input("Enter second string:")
#set=>Sets are used to store multiple items in a single variable. 
#store the string variables at list of strings
list_of_strings=list(set(name_one)&set(name_two))
#print the common elements
print("The common letters are:")
#for loop is iterate the strings one by one
for commonchar in list_of_strings:
#begin for
   #print the common characters
    print(commonchar)
#end for

'''
output:

Enter first string:apple
Enter second string:orange
The common letters are:
a
e
'''