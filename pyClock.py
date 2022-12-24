#importing required libraries
from datetime import datetime
import pygame

#required for setting up the fps
clock=pygame.time.Clock()

#creating the window
screen=pygame.display.set_mode((600,600))

#title of the window
pygame.display.set_caption("D!G!T@L ¢L0¢K")

#initialising pygame
pygame.init()


font=pygame.font.Font("freesansbold.ttf",70)

run=True

#Loop begins
while run:
    #code which exits the window when exit is clicked
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            
    screen.fill("black")
    #to get current time        
    c_time=datetime.now()
    
    #converting it into the font appears on the window
    text=font.render(c_time.strftime("%H:%M:%S"),True,"White")
    
    screen.blit(text,(200,200))
    #here fps is 10
    clock.tick(10)
    
    pygame.display.flip()

pygame.quit()
