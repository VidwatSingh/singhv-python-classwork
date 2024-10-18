import pygame
import random
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

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

x = random.rand
rows = 500
cols = 3   
arr = [None for j in range(rows)]  

arr[3][1] = 1 #assign value at row, column  

for row in range(rows):  
     arr[row][0] = random.randint(0,size[0]-1)
     arr[row][1] = random.randint(0,size[1]-1)
     arr[row][2] = 1
#next row       
print(arr)  


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

    if flake_y > size[1]:
        flake_y = 0
        flake_x = random.randint(0,size[0]-1)
    else:
        flake_y = flake_y + flake_x


    # --- Screen-clearing code goes here
    screen.fill(BLACK)
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.


    # --- Drawing code should go here
    pygame.draw.rect(screen, WHITE, (flake_x,flake_y,5,5))


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()