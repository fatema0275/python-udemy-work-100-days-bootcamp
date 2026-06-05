print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

print("You're on a cross road. Where do you want to go?")
direction = input("\t left or right?\n")
if direction == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    next_step = input("\t Type \"wait\" to wait for the boat. Type \"swim\" to swim across\n")
    if next_step == "wait":
        print("You arrive at the island unharmed. There are 3 house with 3 doors")
        door = input("\t One red, one yellow and one blue. Which color do you choose?\n")
        if door == "yellow":
            print("You found the treasure! You Win!")
        elif door == "red":
            print("Its a room full of fire! You are dead")
        else:
            print("You enter a room of beasts. Game Over")
    else:
        print("You get attacked by an angry trout. Game Over")
else:
    print("You fell in a hole. Game Over")