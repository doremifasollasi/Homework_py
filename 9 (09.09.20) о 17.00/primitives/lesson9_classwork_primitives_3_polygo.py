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

    pygame.draw.polygon(screen, GREEN_COLOR, [[150, 10], [180, 50], [90, 90], [30, 30]], 8)
    # pygame.draw.aalines(screen, GREEN_COLOR, True, [[150, 10], [180, 50], [90, 90], [30, 30]])
    pygame.draw.polygon(screen, WHITE_COLOR, [[250, 110], [280, 150], [190, 190], [130, 130]])
    pygame.draw.aalines(screen, GREEN_COLOR, True, [[250, 110], [280, 150], [190, 190], [130, 130]])

    pygame.display.update()
