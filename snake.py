import pygame , sys, time , random

speed = 15 

# start windows size 

frame_size_x = 720
frame_size_y = 480


check_errors = pygame.init()

if (check_errors[1] > 0 ) :
    print("Error " + check_errors[1])
else : 
    print("Game Succesfully intialized")


pygame.display.set_caption("Snake Game")

Game_window = pygame.display.set_mode(frame_size_x,frame_size_y)

#

black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
red   = pygame.Color(255,0,0)
green = pygame.Color(0,255,0)
blue  = pygame.Color(0,0,255)



