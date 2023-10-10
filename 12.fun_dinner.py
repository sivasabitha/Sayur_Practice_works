'''
Problem 4:
You are reponsible for making dinner for your family. Wrtie all the functions and its input/output.
Eg - buying ingredients, cutting veg, etc.
'''
# first, create a function for buying ingredients
def buy_ingredients(fordinner):
    # initialize the ingredients list 
    ingredients_list = []
    ingredients = fordinner.split(",")
    for item in ingredients:
        # print the buying items
        print("buying " + item)
        # append the items to the ingredients list
        ingredients_list.append(item)
    print("ingredients bought successfully")
    

# second, create a function for cutting the vegetables
def cut_vegetables(vegs):
    # initialize the chopped vegs list 
    chopped_vegs = []
    # split the input to a list of vegetables
    veg_list = vegs.split(",")  
    for veg in veg_list:
        # print the cutting vegetables
        print("cutting " + veg)
        # append the chopped vegetables to the list
        chopped_vegs.append("Chopped " + veg)
    print("vegetables chopped successfully")
    

# third, create a function for cooking dinner
def cook_dinner(dinner_menu):
    # initialize the dinner process list
    dinner_process = []
    # split the input to a list of dishes
    menu_list = dinner_menu.split(",")
    for dish in menu_list:
        # print the cooking dish
        print("Cooking " + dish)
        # append the cooking process
        dinner_process.append("Cooked " + dish)
    print("dinner cooked successfully")

# main program
#get the inputs for ingredients list from user
ingredients_input = input("enter the ingredients you want : ")
#call the buy_ingredients function
ingredients = buy_ingredients(ingredients_input)
#get the inputs vegetables list from user
vegetables_input = input("enter the vegetables you want to cut: ")
#call the cut_vegetables function
chopped_vegetables = cut_vegetables(vegetables_input)
#get the inputs for dinner menu from user
dinner_menu_input = input("enter your dinner menu: ")
#call the cook_dinner function
dinner_menu = cook_dinner(dinner_menu_input)
