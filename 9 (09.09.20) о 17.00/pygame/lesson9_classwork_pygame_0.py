import pygame

WHITE = (255, 255, 255)  
ORANGE = (255, 150, 100)
PURPLE = (128,0,128)
BLUE = (0, 0, 255)
FPS = 60

pygame.init()
gameDisplay = pygame.display.set_mode((600,400))
pygame.display.set_caption("My first game")

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
            print("User asked to quit")
        elif event.type == pygame.KEYDOWN:
            print("User pressed a key.")
        elif event.type == pygame.KEYUP:
            print("User let go of a key.")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("User pressed a mouse button") 

  # --- Game logic should go here
        
    pygame.display.update()
    clock.tick(FPS)