print(''' *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
******************************************************************************* ''')

print("Welcome to Treasure Island."
"Your mission is to find the treasure.")

direction = input("Your are the famous 2-way street where do you want to go? Left or Right: ")

if direction == 'Left':
    task = input("You survived another day!!."
          "Now you are the DEATH lake. What do you choose? Swim or Wait: ")
    if task == 'Wait':
        task1 = input("You have arrived at THE JUDGEMENT GATE!!"
          "Now which gate would you choose? Red or Blue OR Yellow: ")
        if task1 ==  'Yellow':
            print("You win!")
        elif task1 ==  'Red':
            print("Burned by fire. Game Over!")
        elif task1 ==  'Blue':
            print("Eaten by beasts.Game Over!")
        else:
            print("Game Over!")
    else:
        print("Attacked by trout.Game Over!")
else:
    print("Opps!! you fall into the hole. GAME OBER!!")
    


