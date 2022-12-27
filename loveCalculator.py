# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
trueCount = 0
loveCount = 0
loveScore = 0

combinedName = f"{name1}{name2}"
combinedName_lower = combinedName.lower()


trueCount += combinedName_lower.count("t") + combinedName_lower.count("r") + combinedName_lower.count("u") + combinedName_lower.count("e")
loveCount += combinedName_lower.count("l") + combinedName_lower.count("o") + combinedName_lower.count("v") + combinedName_lower.count("e")

loveScore = int(f"{trueCount}{loveCount}")
#print(type(loveScore))

if loveScore < 10 or loveScore > 90:
  print(f"Your score is {loveScore}, you go together like coke and mentos.")
elif loveScore > 40 and loveScore < 50:
  print(f"Your score is {loveScore}, you are alright together.")
else:
  print(f"Your score is {loveScore}.")