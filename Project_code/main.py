# Import the pygame library and initialise the game engine
import pygame
import OpenGL.GL as gl
from OpenGL.GLU import *
from pygame.locals import *
from midpoint import *
from gamefunctions import *

# ---------- TEAM SELECTION --------------
print("Choose your team:")
print("Available Teams: BRA, ARG, FRN, GER, SPA, POR, NET, CRO, MOR")
Team1 = input("Enter Team 1:")
Team2 = input("Enter Team 2:")
Team1 = Team1.upper()
Team2 = Team2.upper()

pygame.init()
 
# Define some colors
BLACK = (0,0,0)
WHITE = (255,255,255)
 
# Open a new window
WIDTH = 1600
HEIGHT = 1000
size = (WIDTH, HEIGHT)
font = pygame.font.Font('freesansbold.ttf', 32)
screen = pygame.display.set_mode(size, DOUBLEBUF|OPENGL)
pygame.display.set_caption("Pong")
 
# The loop will carry on until the user exits the game (e.g. clicks the close button).
carryOn = True
# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()
B = Ball()


# Score Initialization
T1Score = 0
T2Score = 0
# ----------------------------------------
Turn = 0
GK = GoalKeeper(team = Team1)

res = False
reset = False
dive = False
shotX = 800
shotY = 650
shot_init = False




# -------- Main Program Loop -----------

while carryOn:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
              carryOn = False # Flag that we are done so we exit this loop
    if reset:
        B = Ball()
        Turn = Turn ^ 1
        if Turn:
            GK = GoalKeeper(team = Team2)
        else:
            GK = GoalKeeper(team = Team1)
        
        shotX = 800
        shotY = 650
        reset = False
        dive = False



    # --- Game logic should go here
    keys = pygame.key.get_pressed()

   # Ball Movements
    if not res:   #Not shot yet
        if keys[pygame.K_LEFT] and not shot_init:
            shotX -= 10
        if keys[pygame.K_RIGHT] and not shot_init:
            shotX += 10
        if keys[pygame.K_UP] and not shot_init:
            shotY -= 5
        if keys[pygame.K_SPACE]:
            shot_init = True
    # print(shotX, shotY)\

    #GK_Movements:
    if not dive:
        if keys[pygame.K_a]:
            GK.moveLeft()
            GK.moveLeft()
        if keys[pygame.K_d]:
            GK.moveRight()
            GK.moveRight()
        if keys[pygame.K_q]:
            GK.LeftDive()
            GK.moveDown()
            dive = True
        if keys[pygame.K_e]:
            GK.RightDive()
            GK.moveDown()
            dive = True

    if shot_init:
        e = (((800-shotX)*10)/(900 - shotY )) * 1.2
        if shotX < B.x:
            B.Ball_left(e)
        else:
            B.Ball_right(-1*e)
        B.Ball_up()
        if B.y < shotY or B.y < 30:
            shot_init = False
            res = True
    
    if res:
        # print(shotX, shotY)
        # print(GK.x, GK.y)
        if (375 < shotX < 1225) and (562 > shotY > 262) and not GK.collision(shotX,shotY):
            if Turn:
                T1Score += 1
                print("GOAL!! \n{}: {}".format(Team1,T1Score))
            else:
                T2Score += 1
                print("GOAL!! \n{}: {}".format(Team2,T2Score))
            res = False
        else:
            print("MISS")
            print("Score: \n{}: {} \n{}: {}".format(Team1,T1Score,Team2,T2Score))
            res = False
        reset = True

    


    # --- Drawing code should go here
    background()
    goalPost()
    B.DrawBall()
    GK.Draw()
    draw_score(T1Score,100,100, 50, color=(1,1,0))
    draw_score(T2Score,1400,100,50, color = (0,1,1))
    # print(clock.get_fps())
    # First, clear the screen to black. 
    # screen.fill(BLACK)
    #Draw the net
    # pygame.draw.line    
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
     
    # --- Limit to 60 frames per second
    clock.tick(60)
 
#Once we have exited the main program loop we can stop the game engine:
pygame.quit()