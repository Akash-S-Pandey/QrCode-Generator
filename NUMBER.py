import random
import math

print("\t*****  Welcome To The Number Guessing Game \t *****")

lower = int(input("Enter the Lower bond : "))

upper =int(input("Enter the Upper bond : "))

#Creating the random number
x = random.randint(lower,upper)
print("\n\t\tYou have only",
      round(math.log(upper-lower + 1,2)),
      "Chances to guess the Number"
      )

# creating cound and loop for number input
count = 0

while count < math.log(upper-lower+1,2):
       count+=1
       #taking guessing number ad input
       guess = int(input("Guess a number:- "))

       #creating a loop and condition checking
       if x == guess:
          print("Congratulation user you have done it in",
                count,"attempts")
       # break the loop
          break
       elif x > guess:
          print("you guessed to small !")
       elif x < guess:
          print("you guessed to high ! ")
#here we are creating a logic for chances when gwtting completed
if count >= math.log(upper-lower +1 ,2):
    print("the number is %d" % x)
    print("\t try ur Luck next Time **** ")









