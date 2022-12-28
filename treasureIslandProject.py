print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
#.lower() can be implemented after the input() function vs seperate variables

choice1 = input("You walk through a hidden trail and find yourself lost with two roads ahead of you. Choose your destiny. Do you go with left or right? ")
choice1_lower = choice1.lower()

if choice1_lower == "right":
  print("\nGoing along this road, you find yourself falling into a pit of despair with no way out. You lose all hope and when you think things get worse, they do. You lose consciousness and wake up being eaten by a zombie. Game Over.")
elif choice1_lower == "left":
  choice2 = input("\nFollowing your instincts, you hear noises coming from behind you, getting closer each moment. You feel like you are in danger. With being in a dead end, you see a lake in which you can swim across. You feel like you can wait and stay quiet but the risks are costly. Do you swim or wait? ")
  choice2_lower = choice2.lower()
  
  if choice2_lower == "swim":
      print("\nHalfway across the lake, you get attacked by a zombie shark. Game Over.")
  elif choice2_lower == "wait":
    choice3 = input("\nYou have chosen to wait.. good choice.. in a distance you see a couple of doors coming from several sheds. If only you can find a way to get help and reach to safety. Red, Blue, or Yellow. Which door do you choose? ")
    choice3_lower = choice3.lower()
    
    if choice3 == "red":
      print("\nYou get ambushed by a horde of zombies. Game Over.")
    elif choice3 == "blue":
      print("\nYou get attacked by a bear. Game Over.")
    elif choice3 == "yellow":
      print("\nYou find the treasure and head back to safety. You Win!")
