#import random module
import random as rd

#lenght of the password
len=int(input("enter the length of the password you need to generate: "))

#password characters
char="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@#&*!_/"

#main func
def generate_password(len):
    password=""
    for i in range(len):
        password+=rd.choice(char)
    return password

pswd=generate_password(len)

#for neatness
print("")

print("your password has been generated.Your Password is: "+pswd)
        