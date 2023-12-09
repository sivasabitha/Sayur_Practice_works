'''
Problem #1
You have a list of numbers in ascending order, but with duplicates.
Remove the duplicated, append _ at the end for each duplicate removed 
eg input = [1,2,3,3,3,4,4,7,7,9]
output = [1,2,3,4,7,9,_,_,_,_]
'''
#create the list
def remove_duplicates(input_list):
    #count the duplicate like {3:2,4:1}
    duplicates_count = {}
    result_list = []
    for num in input_list:
        #check the num is not in duplicate dict
        if num not in duplicates_count:
            result_list.append(num)
            #all the num are take count then we check it
            duplicates_count[num] = 1
        else:
            duplicates_count[num] += 1
    print(duplicates_count)
    #iterate the duplicate_count dict
    for key in duplicates_count:
        #if count is greater than 1 then add the '_' at end of the list
        if duplicates_count[key] > 1:
            result_list.extend(['_'] * (duplicates_count[key] - 1))
    return result_list

#initialize the input_list 
input_list = [1, 2, 3, 3, 3, 4, 4, 7, 7, 9]
#call the function
output_list = remove_duplicates(input_list)
print(output_list)

'''
output:

{1: 1, 2: 1, 3: 3, 4: 2, 7: 2, 9: 1}
[1, 2, 3, 4, 7, 9, '_', '_', '_', '_']
'''