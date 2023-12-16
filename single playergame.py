'''
Problem #3
Its is a single player game where the user starts with 0 points. User keeps rolling the 
dice.If the rolled number is 0, game ends. If the rolled number is even, then 2 points are
 added. If the number is odd, then if the number is 1,3 then the user has to jump. 
 If the number is 5, then 3 points are added. The game ends when the user has 50 points.
'''
#import random function
import random

#function for rolling dice
def roll_dice():
    return random.randint(0, 6)

player_point=0
total_points=50
while(True):
    #The game ends when the user has 50 points
    if(player_point>=50):
        break
    #give the message for user to press enter to roll the dice
    input(f"player, press enter to roll the dice ")
    #step 1: roll the dice
    rolled_num = roll_dice()
    print(f"player rolled: ({rolled_num})")
    
    #If the rolled number is 0, game ends
    if(rolled_num==0):
        print("your game is end")
        break
    #If the rolled number is even, then 2 points are added.
    elif(rolled_num%2==0):
        player_point+=2
    #if the number is 1,3 then the user has to jump
    elif((rolled_num==1)or (rolled_num==3)):
        continue
    #If the number is 5, then 3 points are added
    elif(rolled_num==5):
        player_point+=3
    else:
        continue
print(f"player_point: {player_point}")

'''
output:

player, press enter to roll the dice 
player rolled: (5)
player, press enter to roll the dice
player rolled: (4)
player, press enter to roll the dice
player rolled: (6)
player, press enter to roll the dice
player rolled: (1)
player, press enter to roll the dice
player rolled: (0)
your game is end
player_point: 7
'''

