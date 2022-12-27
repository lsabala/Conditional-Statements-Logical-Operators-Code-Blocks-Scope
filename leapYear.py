#This is how you work out whether if a particular year is a leap year.
#on every year that is evenly divisible by 4 

#except** every year that is evenly divisible by 100 
#unless** the year is also evenly divisible by 400
#Figure out logic before starting to code - flowchart

# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if year % 4 == 0 and year % 100 != 0:
      print("Leap year.")
elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
      print("Leap year.")
else:
  print("Not leap year.")


