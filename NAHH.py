import pygame
import random
import math
pygame.init()
screen = pygame.display.set_mode((800, 800))
screen.fill((0, 0, 0))
pygame.display.set_caption("Randon Circles")

#add the collision function definition here
def randoncircles(cx,cy,x,y,r):
    if math.sqrt((cx-x)**2+(cy-y)**2)< r:
        return True
    
    
#mouse variables
xpos = 0
ypos = 0
collide = False

#cirlce variables
cirX = 400
cirY = 400 
size = 30
score = 0
r = 255
g = 255
b = 255

#seed = int(input("Input a seed\n"))
#random.seed(seed)

mousePos = (xpos, ypos) 
click = False

BLUE = (0,0,200)
RED = (200, 0,0)
GREEN = (0,200, 0)
YELLOW = (200, 200, 0)
PURPLE = (200, 0, 200)
TEAL = (0,200,200)
WHITE = (255, 255, 255)
BLACK = (0,0,0)
color = RED

while True: #OMG GAME LOOP##################################################################
    
    #input section-------------------------------------
    event = pygame.event.wait()

    if event.type == pygame.QUIT: 
        break

    if event.type == pygame.MOUSEBUTTONDOWN:#when you click
       mousePos = event.pos#get a snapshot of the position
       click = True
    else:
        click = False 
        
    #if event.type == pygame.MOUSEBUTTONUP:
     #   draw = False

    #if event.type == pygame.MOUSEMOTION:
     #   mousePos = event.pos

    #logic/movement/physics section-----------------------
        
    #call function IN an if statement, reset random numbers if it returns true
    x,y = pygame.mouse.get_pos()
    if  randoncircles(cirX,cirY,x,y,size)== True and click == True:
        size = random.randrange(20,50)
        cirX = random.randrange(size,800-size)
        cirY = random.randrange(size,800-size)
        score += 1


    #graphics section--------------------------------------
    screen.fill((0,0,0)) 
    pygame.draw.circle(screen, (r, g, b), (cirX, cirY), size)

   

    



    pygame.display.flip()

#pygame.quit()
