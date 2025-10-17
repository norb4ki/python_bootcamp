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
direction = input('You are at a cross road. Where do you want to go?\nType "left" or "right"\n')
if direction == 'left':
    action = input('You see an island with a boat next to it. What are  you going to do?\nPrint "wait" to wait for a boat, "swim" to swim across the lake\n')
    if action == 'wait':
        door = input('You see a house with 3 doors in it. Which one are you choosing: "yellow", "green" or "blue"?\n'        )
        if door == 'blue':
            print('You was eaten by wild rabbits that were hiding in the room. \nGame Over')
        elif door == 'yellow':
            print('You found the room full of treasures. \nNow you have to pay half of it to the government as a tax and hope to not get shot by criminals.\nGame Over')
        elif door == 'red':
            print('You wan burned by fire.\nGame Over')
        else:
            print('The real treasure is the memories you got along the way. You won!')
    else:
        print('You was tickled to death by golden fish!\nGame over')
else:
    print('You was watching the stars and fell to a hole. Game Over')