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


#start colors set
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
red   = pygame.Color(255,0,0)
green = pygame.Color(0,255,0)
blue  = pygame.Color(0,0,255)
#endcolors set

fps_controller = pygame.time.Clock()

#one snake square size
square_size = 20 


#Start snake info Function
def init_vars():
   global head_pos , snake_body , food_pos, food_spawn , score , direction 
   direction  = "RIGHT"
   head_pos   = [120,60]
   snake_body = [[120 , 60]]
   food_pos   = [random.randrange(1,(frame_size_x // square_size)) * square_size, 
                 random.randrange(1,(frame_size_y // square_size)) * square_size]
   food_spawn = True
   score      = 0


init_vars()

#End Snake info Function 

#Start Show Score Function
def Show_Score():
    print("Showing Score : ")

#End Show Score Function 

#Start Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        elif event.type == pygame.KEYDOWN:
                if(event.key == pygame.K_UP or event.key == ord("w") and direction != "DOWN"):
                    direction = "UP"
                elif (event.key == pygame.K_DOWN or event.key == ord("s") and direction != "UP"):
                    direction = "DOWN"
                elif (event.key == pygame.K_LEFT or event.key == ord("a") and direction != "RIGHT"):
                    direction = "LEFT"
                elif (event.key == pygame.K_RIGHT or event.key == ord("d") and direction != "LEFT"):
                    direction = "RIGHT"
#End Game Loop

    if direction == "UP" :
         head_pos[1] -= square_size
    elif direction == "DOWN":
         head_pos[1] += square_size
    elif direction == "LEFT" : 
         head_pos[0] -= square_size
    elif direction == "RIGHT":
         head_pos[0] += square_size


    if head_pos[0] < 0:
         head_pos[0] = frame_size_x - square_size
    elif head_pos[0] > frame_size_x - square_size:
         head_pos[0] = 0
    elif head_pos[1] <0 :
         head_pos[1] = frame_size_y - square_size
    elif head_pos[1] > frame_size_y - square_size:
         head_pos[1] = 0

#Start eating apple 
    snake_body.insert(0, list(head_pos))
    if head_pos[0] == food_pos[0] and head_pos[1] == food_pos[1]:
            score += 1
            food_spawn = False
    else:
            snake_body.pop()
# End  eating apple