'''
Problem #1
Write the dictionaty structure for storing recipes for food.
Hardcode your own data.
Get user input for the name of the recipe, and then print the recipe. 
Eg: Input : Idli
Output : Here is the recipe for idli. 
You need ingrediants Rice and Dal.
 The procedure to cook is grind rice and dal, ferment and steam.
Input : Yogurt rice
Output :  Here is the recipe for Yogurt rice. 
You need ingrediants Rice and yogurt.
The procedure to cook is cook rice first and then add yogurt.
'''
#create the dictionary
recipes_dict={
    "idli":"You need ingrediants Rice and Dal. The procedure to cook is grind rice and dal, ferment and steam.",
    "yogurt rice":"You need ingrediants Rice and yogurt.The procedure to cook is cook rice first and then add yogurt.",
    "lemon rice":"you need ingredients rice and lemon. The procedue to cook is cook rice fist and then add lemon"
}
#get the nput from user
user_input=input("enter the recipe you want: ")
#print the user needed recipes and procedures
print(f"here is the recipe for {user_input} :\n {recipes_dict[user_input]} ")

'''
output:

enter the recipe you want: lemon rice
here is the recipe for lemon rice :
 you need ingredients rice and lemon. The procedue to cook is cook rice fist and then add lemon 
'''
