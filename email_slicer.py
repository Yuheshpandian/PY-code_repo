#import d_print func
from delay_print import d_print
#input of the code
e_mail=input("enter you e_mail address: " )

name=""
#code for getting the name
for x in e_mail:
    if x=="@":
        break
    else:
        name+=x
#domain is which mail you are using
domain=e_mail[e_mail.index("@")+1:]

d_print(f"Hi Mr/Ms {name} hope you enjoy our service.This program is created by Mr yuhesh pandian in pytho.We'll reach you in {domain}")
