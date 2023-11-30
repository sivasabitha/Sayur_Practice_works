'''
Problem #1
write a program that reads a passage and reverses the order of 
letters in each word while keeping the word order intact. Use function.
Eg- input - I am Sayur
Output I ma ruyaS
'''
#create a function for reversed string
def reverse_words(input_string):
    #split the string into words
    words = input_string.split()
    reversed_words = []
    for word in words:
        #use slice function for reverse process then append the reversed words
        reversed_word = word[::-1]
        reversed_words.append(reversed_word)
    #join the words 
    reversed_string = ' '.join(reversed_words)
    return reversed_string
#get the input stinr from user
input_string = input("Enter the string: ")
#call the function then print the result
reversed_string = reverse_words(input_string)
print("reversed string: ", reversed_string)



