# importing libraries
import time
import pyttsx3

# initialising
engine = pyttsx3.init()

# the number to count
duration = int(input('enter tne number that I need to count: '))

# main loop 
for n in range(duration):
    print(n+1, end = '\r')
    engine.say(str(n+1))
    engine.runAndWait()
    
    # time pause
    time.sleep(0.02)


print('TIME OVER')
