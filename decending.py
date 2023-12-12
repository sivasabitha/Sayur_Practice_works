'''
problem #2
Same as above,but print the list in descending order
input = [1,2,3,3,3,4,4,7,7,9]
output = [9,7,4,3,2,1,_,_,_,_]
'''
#create the list
def remove_duplicates(input_list):
    #count the duplicate like {3:2,4:1}
    duplicates_count = {}
    result_list = []
    #sort the list then reversed the list then we get the decending ordered list
    input_list=sorted(input_list)
    for num in reversed(input_list):
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
input_list = [111, 22, 345, 335, 32, 4, 4, 7, 7, 9]
#call the function
output_list = remove_duplicates(input_list)
print(output_list)

'''
output:

{345: 1, 335: 1, 111: 1, 32: 1, 22: 1, 9: 1, 7: 2, 4: 2}
[345, 335, 111, 32, 22, 9, 7, 4, '_', '_']
'''