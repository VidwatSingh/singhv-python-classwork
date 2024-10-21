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

class Flake: # this is a record
        def __init__(self,x_pos,y_pos,velocity,size) -> None:
             self.x = x_pos
             self.y = y_pos
             self.v = velocity
             self.s = size
        #end fields
#end record

pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Snow")

### SRC - This code sets up a 2D array, one dimension for the rows
### The other dimension stores the 3 values for the snowflake.
### You need to change this to be just a 1D array. 
rows = 50
arr = [None] * rows  # Change this line to have 50 values of None 


### SRC - This is where we are updating the array to have random values for our flakes
x = random.randint(0, size[0] - 1)
y = random.randint(0,size[1] - 1)
v = random.randint(2,5)
s = random.randint(2,5)

for row in range(rows):  
     # SRC - I've added the code to create a Flake record below:
     my_flake = Flake(x,y,v,s) # SRC - You need to set the right values for x, y, v and s
     ### then change the lines below to add my_flake to the 1D array. 
     arr[row] = my_flake
     #arr[row][0] = random.randint(0,size[0]-1)
     #arr[row][1] = random.randint(0,size[1]-1)
     #arr[row][2] = 1


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
        if arr[i].y > size[1]: ### It#s not flake.y but arr[i].y etc.
              arr[i].y = random.randint(0, 100)
              arr[i].x = random.randint(0, size[0] - 1)
              arr[i].s = random.randint(2,5)
              arr[i].v = random.randint(2,5)
        else:
             arr[i].y = arr[i].y + arr[i].v
    
    # --- Screen-clearing code goes here
    screen.fill(BLACK)
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.


    # --- Drawing code should go here
    ### Again here it's not flake.x etc you need to access the flakes in the array.
    for i in range(len(arr)):
        pygame.draw.rect(screen, WHITE, (arr[i].x,arr[i].y,arr[i].s,arr[i].s))


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()