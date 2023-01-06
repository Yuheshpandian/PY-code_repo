#import Python inbuilt lib random
import random as rd

#the Number 
num = rd.randint(0,1000)

print(f"your Number has {len(str(num))} digits\n")

#Loop begins
for x in range(10,0,-1):
    print(f"you have {x} chances \n")
    guess =int(input("Enter your guess:"))
    print("")
    if guess>num:
        print("Your guess is BİG  •_• \n")
    if guess<num:
        print("your guess is small '_' \n")
    if guess==num:
        print(f" You found it ^_^.The Number is {num}")
        break
else:
    print(f"The Number is {num}")        