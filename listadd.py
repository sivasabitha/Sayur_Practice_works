'''
Problem #3 
Add two number represented in a list as reversed. print the sum also as a list in reverse order
eg input list1 = [1,2,3] list2 = [5,6,7]
answer= [6,8,0,1]
 explanation (321 + 765 = 1086)
'''
#reverse the list function
def reverse(input_list):
   new_list = input_list[::-1]
   return new_list

#Add two number represented in a list as reversed. print the sum also as a list in reverse order
#create a list 
def list_add_res_rev(list1,list2):
    #map list into string
    list1=map(str,list1)
    list2=map(str,list2)
    #join the  string 
    list1 = "".join(list1)
    list2 = "".join(list2)
    #reverse the string
    list1=reverse(list1)
    list2=reverse(list2)
    print("list1,list2",list1,list2)
    #add the list1 and list2 change these list into integer
    addition=int(list1)+int(list2)
    print("addition",addition)
    #int: to each character in use of map function , to map interger to list then reverse it
    result = list(map(int,str(addition)))
    print("result:",result)
    result=reverse(result)
    print(result)
    return result
#get the list from user
list1=list(map(int,input("enter the list1: ").split()))
list2 =list(map(int,input("enter the list2: ").split()))
#call thefunction then print 
add=list_add_res_rev(list1,list2)
print("final result: ",add)

'''
output:

enter the list1: 1 2 3
enter the list2: 5 6 7
list1,list2 321 765
addition 1086
result: [1, 0, 8, 6]
[6, 8, 0, 1]
final result:  [6, 8, 0, 1]
'''