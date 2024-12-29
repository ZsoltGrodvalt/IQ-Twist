import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
RED = (205,0,0)
GREEN = (50,205,50)
BLUE = (0,0,205)
YELLOW = (255,215,0)

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("IQTwist")

piece_list = [pygame.Rect(0, 100, 100, 100),
              pygame.Rect(100, 100, 100, 100),
              pygame.Rect(200, 100, 100, 100),
              pygame.Rect(300, 100, 100, 100)]

color_list = [RED,GREEN,BLUE,YELLOW]
color_var = 0

window.fill((255, 255, 255))

for piece in piece_list:
    # print(color_var)
    pygame.draw.rect(window, color_list[color_var],piece)
    color_var += 1

run = True
while run: 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()