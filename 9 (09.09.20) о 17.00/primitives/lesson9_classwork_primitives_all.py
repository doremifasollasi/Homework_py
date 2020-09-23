import pygame

WIDTH_DISPLAY=500
HEIGHT_DISPLAY=500

WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
GRAY_COLOR = (125, 125, 125)
LIGHT_BLUE_COLOR = (64, 128, 255)
GREEN_COLOR = (0, 200, 64)
YELLOW_COLOR = (225, 225, 0)
PINK_COLOR = (230, 50, 230)
PI = 3.14

pygame.init()

screen = pygame.display.set_mode((WIDTH_DISPLAY,HEIGHT_DISPLAY))

pygame.display.set_caption("Draw primitives")

clock = pygame.time.Clock()

done = False

while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done = True

    pygame.draw.line(screen, (255,255,255), [10, 30], [290, 15], 3)
    pygame.draw.rect(screen, (255,0,0), [55, 50, 80, 55])
    pygame.draw.rect(screen, (0,0,128), [175, 130, 80, 55]) 
    pygame.draw.rect(screen, (64, 128, 255), (300, 70, 100, 75), 8)
    pygame.draw.aalines(screen, (255,255,255), True, [[250, 210], [280, 250], [190, 290], [180, 280]])  
    pygame.draw.circle(screen, (192,192,192), (300, 300), 50)
    pygame.draw.circle(screen, (255,255,0), (80, 250), 50, 10)
    
    pygame.display.update()
    # clock.tick(60)