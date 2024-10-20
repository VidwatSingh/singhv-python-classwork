import pygame
import random
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

x_pos = random.randint(0,700)
y_pos = random.randint(0, 500)
velocity = random.randint(1,10)

class flake: # this is a record
        def __init__(self,x_pos,y_pos,velocity,size) -> None:
             self.x = x_pos
             self.y = y_pos
             self.vel = velocity
             self.size = size
        #end fields
#end record

pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Snow")

rows = 50
cols = 3   
arr = [[0 for i in range(cols)] for j in range(rows)]  



for row in range(rows):  
     arr[row][0] = random.randint(0,size[0]-1)
     arr[row][1] = random.randint(0,size[1]-1)
     arr[row][2] = 1


# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    for i in range(len(arr)):
        if flake.y > size[1]:
              flake.y = 0
              flake.x = random.randint(0,size[0]-1)
        else:
             flake.y += flake.vel
    
    # --- Screen-clearing code goes here
    screen.fill(BLACK)
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.


    # --- Drawing code should go here
    for i in range(len(arr)):
        pygame.draw.rect(screen, WHITE, (flake.x,flake.y,flake.size,flake.size))


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()