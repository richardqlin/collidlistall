import pygame
import random
import time
from pygame.locals import *
import random


pygame.init()


s=[1,-1]
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
white=(255,255,255)
black=(0,0,0)

white=(255,255,255)
width=640
height=480

screen=pygame.display.set_mode((width,height))
pygame.display.set_caption('Pong Game')
font=pygame.font.SysFont(None,25)

platform=pygame.Rect(200,450,120,40)

circle_list=[]
circle_list1=[]
for i in range(1):
    circle_1=pygame.draw.circle(screen,'red',(random.randint(0,500), random.randint(0,300)),25)
    circle_list.append([random.randint(0,500), random.randint(0,300)])
    circle_list1.append(circle_1)

f=[red,green]
f=random.choice([red,green])
while 1:
    screen.fill(black)
    pygame.time.delay(10)
    for i in circle_list:
        
        pygame.draw.circle(screen,f,i,25)
        
        i[1]+=1
        if i[1]==480:
            i[1]=0
            i[0]=random.randint(0,500)
            f=random.choice([red,green])
        
    for i in circle_list1:
        pygame.draw.rect(screen,red,i)
        i[3]+=1
        
    platform= pygame.draw.rect(screen, blue,(200,450,120,40))

    if platform.collidelistall(circle_list1):
        f=random.choice([red,green, blue])
        circle_1=pygame.draw.circle(screen,f,(random.randint(0,500), random.randint(0,300)),25)  
        circle_list1.append(circle_1)
        print('coll')
    #pygame.display.flip()
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    
