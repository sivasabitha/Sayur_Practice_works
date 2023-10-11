'''
Problem #2
Write the dictionaty structure for storing recipes for food.
Hardcode your own data.
User input is any ingredient. List all the recipes that include the ingredient
Input : Rice
Output : You can make Idli and Yogurt rice with rice.
'''
#create a dictionary for ingredients
ingredient_dict={
    "rice":"idli and yogurt rice ",
    "potato":"frys and bajji ",
    "chicken":"fried rice and biryani "
}
#get the ingredients from the user
user_input=input("enter the ingredient you want: ")
#print the user needed recipes with their choice of ingredient
print(f"you can make {ingredient_dict[user_input]} with {user_input}")

'''
output:

enter the ingredient you want: potato
you can make frys and bajji  with potato
'''