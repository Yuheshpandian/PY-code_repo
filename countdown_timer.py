import time
import pyttsx3

engine = pyttsx3.init()

duration = int(input('enter tne number that I need to count: '))

for n in range(duration):
    print(n+1, end = '\r')
    engine.say(str(n+1))
    engine.runAndWait()
    
    
    time.sleep(0.02)

print('TIME OVER')