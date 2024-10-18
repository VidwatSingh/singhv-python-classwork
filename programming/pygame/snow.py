import pygame
import random

# Define some colors
BLACK = 0x000000
WHITE = 0xFFFFFF
x = 100
y = 0
x2 = 50
y2 = 0
x3 = 250
y3 = 0


pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Snow")

# Initialise flake variables here to have random initial position:
# x, y, velocity


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
    if y >= 480:
        y = 0
        x = random.randint(0,680)
    elif y >= 0 and y < 480:
        y += 1

    if y2 >= 480:
        y2 = 0
        x2 = random.randint(0,680)
    elif y2 >= 0 and y2 < 480:
        y2 += 1

    if y3 >= 480:
        y3 = 0
        x3 = random.randint(0,680)
    elif y3 >= 0 and y3 < 480:
        y3 += 1

    # --- Screen-clearing code goes here
    screen.fill(BLACK)
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.


    # --- Drawing code should go here
    pygame.draw.ellipse(screen, WHITE, [x,y,5,5], 0)
    pygame.draw.ellipse(screen, WHITE, [x2,y2,5,5], 0)
    pygame.draw.ellipse(screen, WHITE, [x3,y3,5,5], 0)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()