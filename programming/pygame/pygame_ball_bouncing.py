import pygame
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
x_pos_ball = 350
y_pos_ball = 250
yballdir = 1
xballdir = 1
ballspeed = 5
pygame.init()
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")
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
    if y_pos_ball >500 or y_pos_ball<0:
        yballdir *=-1
    if x_pos_ball > 700 or x_pos_ball < 0:
        xballdir *= -1


    y_pos_ball = y_pos_ball+(ballspeed*yballdir)
    x_pos_ball = x_pos_ball + (ballspeed * xballdir)
    # --- Screen-clearing code goes here
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
    # --- Drawing code should go here
    pygame.draw.ellipse(screen, RED, [x_pos_ball,y_pos_ball,20,20], 0)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    # --- Limit to 60 frames per second
    clock.tick(60)
# Close the window and quit.
pygame.quit()
 