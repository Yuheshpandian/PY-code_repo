#importing required libraries 
import sys
import time as t

#input of the code
text=input("Enter the word or sentence that you want to see printed in unique manner: ")


#code for delay_printing
def d_print(x):
    for i in x:
        sys.stdout.write(i)
        sys.stdout.flush()
        t.sleep(0.07)
        
#for neatness
print("")        

#calling the function        
d_print(text)