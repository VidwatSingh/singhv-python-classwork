import pygame
pygame.init
BLACK = (   0,  0,    0)
WHITE = (0xFF, 0XFF, 0XFF)
GREEN = (   0, 255,   0)
RED   = ( 255,    0,  0)
BLUE  = (   0,  0,  255)
done = False
PI = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
clock = pygame.time.Clock()
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Vidwat's Game Code")
screen.fill(WHITE)
x = 50
y= 50
R = 25
E = 25
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
            print("User asked to quit.")
 
    # --- Game logic should go 
    x += 1
    if x > 680:
        x = 1
    # --- Drawing code should go here
    # draw a rectangle

    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
    pygame.draw.rect(screen,RED,[x, y,R,E],0)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)