import pygame
import random

# Define some colors
BLACK = 0x000000
WHITE = 0xFFFFFF

class Flake: # This is a Class
    def __init__(self) -> None:
        self.x = random.randint(0,screen_size[0]-1)
        self.y = random.randint(0,screen_size[1]-1)
        type = random.choice(['slow','medium','fast'])
        match type:
            case 'fast':
                self.vel = 3
                self.size = 4
            case 'medium':
                self.vel = 2
                self.size = 6
            case 'slow':
                self.vel = 1
                self.size = 8
        #end switch
    # End fields

    def fall(self):
        if self.y > screen_size[1]:
            self.y = 0
            self.x = random.randint(0,screen_size[0]-1)
        else:
            self.y = self.y + self.vel
        #end if
    #end method

    def draw(self):
        pygame.draw.ellipse(screen, WHITE, (self.x,self.y,self.size,self.size))  
    #end method



#end record


pygame.init()

# Set the width and height of the screen [width, height]
screen_size = (700, 500)
screen = pygame.display.set_mode(screen_size)

pygame.display.set_caption("Snow")


number_of_flakes = 500 
flakes = [None for j in range(number_of_flakes)]  

#arr[3][1] = 1 #assign value at row, column  

for row in range(number_of_flakes):  
    my_flake = Flake()
    flakes[row] = my_flake
#next row       
#print(arr)  


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
    for flake in flakes:
        flake.fall()


    # --- Screen-clearing code goes here
    screen.fill(BLACK)
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.


    # --- Drawing code should go here
    for flake in flakes:
        flake.draw()

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()