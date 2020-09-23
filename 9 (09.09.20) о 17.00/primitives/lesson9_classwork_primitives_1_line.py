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

done = True    # False

while done:     # not done
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done = False   # True
    
    
    # pygame.draw.line(screen, (255,255,255), [10, 30], [290, 15], 3)
    pygame.draw.line(screen, WHITE_COLOR, [10, 30], [290, 15], 3)
    pygame.draw.line(screen, WHITE_COLOR, [10, 80], [320, 55])
    
    # aaline згладжена лінія, товщина в цьому випадку не задається
    # pygame.draw.aaline(screen, WHITE_COLOR, [10, 70], [290, 55])
   
    pygame.display.update()













# import pygame

# WIDTH_DISPLAY = 500
# HEIGHT_DISPLAY = 500

# WHITE_COLOR = (255, 255, 255)
# BLACK_COLOR = (0, 0, 0)
# GRAY_COLOR = (125, 125, 125)
# LIGHT_BLUE_COLOR = (64, 128, 255)
# GREEN_COLOR = (0, 200, 64)
# YELLOW_COLOR = (225, 225, 0)
# PINK_COLOR = (230, 50, 230)
# PI = 3.14

# pygame.init()

# screen = pygame.display.set_mode((WIDTH_DISPLAY,HEIGHT_DISPLAY))

# pygame.display.set_caption("Draw primitives")

# clock = pygame.time.Clock()

# done = True

# while done:
#     for event in pygame.event.get(): 
#         if event.type == pygame.QUIT:
#             done = True
    
#     # прямокутник rectangle
#     # pygame.draw.rect(screen, PINK_COLOR, (20, 20, 100, 75))
#     # pygame.draw.rect(screen, (64, 128, 255), (150, 20, 100, 75), 8)

#     # дуги ark
#     # pygame.draw.arc(screen, WHITE_COLOR, (10, 50, 280, 100), 0, PI)
#     # pygame.draw.arc(screen, PINK_COLOR, (50, 30, 200, 150), PI, 2*PI, 3)

#     # circle
#     # pygame.draw.circle(screen, YELLOW_COLOR, (100, 100), 50,5)
#     # pygame.draw.circle(screen, PINK_COLOR, (400, 200), 50)

#     # ellipse
#     # pygame.draw.ellipse(screen, GREEN_COLOR, (10, 50, 280, 100))

#     # all primitives
#     pygame.draw.line(screen, (255,255,255), [10, 30], [290, 15], 3)
#     pygame.draw.rect(screen, (255,0,0), [55, 50, 80, 55])
#     pygame.draw.rect(screen, (0,0,128), [175, 130, 80, 55]) 
#     pygame.draw.rect(screen, (64, 128, 255), (300, 70, 100, 75), 8)
#     pygame.draw.aalines(screen, (255,255,255), True, [[250, 210], [280, 250], [190, 290], [180, 280]])  
#     pygame.draw.circle(screen, (192,192,192), (300, 300), 50)
#     pygame.draw.circle(screen, (255,255,0), (80, 250), 50, 10)


#     #
#     # pygame.draw.polygon(screen, GREEN_COLOR, [[150, 10], [180, 50], [90, 90], [30, 30]],8)
#     # # pygame.draw.polygon(screen, GREEN_COLOR, [[250, 110], [280, 150], [190, 190], [130, 130]])
#     # pygame.draw.aalines(screen, GREEN_COLOR, False, [[250, 110], [280, 150], [190, 190], [130, 130]])


#     #
#     #pygame.draw.line(screen, (255,255,255), [10, 30], [290, 15], 3)
#     # pygame.draw.line(screen, WHITE_COLOR, [10, 30], [290, 15], 3)
#     # pygame.draw.line(screen, WHITE_COLOR, [10, 80], [320, 55])
    
#     #
#     #aaline згладжена лінія, товщина в цьому
#     # випадку не задається
#     # pygame.draw.aaline(screen, WHITE_COLOR, [10, 70], [290, 55])
   
#     pygame.display.update()