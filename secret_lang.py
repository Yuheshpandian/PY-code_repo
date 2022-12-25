#this dict helps us to translate the normal message/coded message to coded message/normal message
lang={"a":"z","b":"y","c":"x","d":"w","e":"v","f":"u","g":"t","h":"s","i":"r","j":"q","k":"p","l":"o","m":"n","n":"m","o":"l","p":"k","q":"j","r":"i","s":"h","t":"g","u":"f","v":"e","w":"d","x":"c","y":"b","z":"a"," ":";","'":"&",".":"#"}

#func that encrypt's a message
def code(text):
    x=""
    for val in text.lower():
        try:
            x+=lang[val]
        except:
            return "invalid message,cant able to code"
    return x
    
#func that decrypt's a code    
def decode(text):
    x=""
    for val in text.lower():
        for key,value in lang.items():
            if val==value:
                x+=key 
    else:
        return "invalid message,cant able to decode"       
    return x
    
#uncomment the next comment to encrypt a message         
"""
text=input("enter the sentence or message you need to code:")
text=code(text)
print(text)
"""
#uncomment the next comment to encrypt a message
"""
text=input("enter the sentence or message you need to decode:")
text=decode(text)
print(text)
""" 
#thankyou 
