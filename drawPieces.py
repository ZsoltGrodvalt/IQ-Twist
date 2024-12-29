import pygame

SCREEN_WIDTH = 100
SCREEN_HEIGHT = 100
RED = (205,0,0)
GREEN = (50,205,50)
BLUE = (0,0,205)
YELLOW = (255,215,0)
GRAY = (105,105,105)
BLACK = (0,0,0)
BLOCK_SIZE = 100

def coord2poly(coordinates:list[tuple[int]],blockSize:int):
    '''Multiplies the list of tuples with a scalar value.

    Eg. [(1,2),(3,4)] -> [(100,200),(300,400)] 
    '''
    poly = []
    for point in coordinates:
        poly.append((point[0]*blockSize,point[1]*blockSize))
    return poly


def RedL():
    # Rectangles
    pygame.draw.rect(surface, RED, pygame.Rect(0,0,300,100),border_top_left_radius=50, border_top_right_radius=50, border_bottom_left_radius=-1, border_bottom_right_radius=50)
    pygame.draw.rect(surface, RED, pygame.Rect(0,100,100,100),border_top_left_radius=-1, border_top_right_radius=-1, border_bottom_left_radius=50, border_bottom_right_radius=50)

    # Holes
    hole_list = [[(50,50),40],
                [(250,50),40]]
    for hole in hole_list:
        pygame.draw.circle(surface, BLACK, hole[0],hole[1])

    # pygame.draw.polygon(surface, GRAY, polygon,width=10)
    pygame.image.save(surface,'RedL.png')

def RedZ():
    # Rectangles
    pygame.draw.rect(surface, RED, pygame.Rect(0,0,200,100),border_top_left_radius=50, border_top_right_radius=50, border_bottom_left_radius=50, border_bottom_right_radius=-1)
    pygame.draw.rect(surface, RED, pygame.Rect(100,100,200,100),border_top_left_radius=-1, border_top_right_radius=50, border_bottom_left_radius=50, border_bottom_right_radius=50)

    # Holes
    hole_list = [[(150,150),40]]
    for hole in hole_list:
        pygame.draw.circle(surface, BLACK, hole[0],hole[1])

    # pygame.draw.polygon(surface, GRAY, polygon,width=10)
    pygame.image.save(surface,'RedZ.png')

def Green3():
    # Rectangles
    pygame.draw.rect(surface, GREEN, pygame.Rect(0,0,200,100),border_top_left_radius=50, border_top_right_radius=50, border_bottom_left_radius=50, border_bottom_right_radius=-1)
    pygame.draw.rect(surface, GREEN, pygame.Rect(100,100,100,100),border_top_left_radius=-1, border_top_right_radius=-1, border_bottom_left_radius=50, border_bottom_right_radius=50)

    # Holes
    hole_list = [[(50,50),40],
                 [(150,50),40]]
    for hole in hole_list:
        pygame.draw.circle(surface, BLACK, hole[0],hole[1])

    # pygame.draw.polygon(surface, GRAY, polygon,width=10)
    pygame.image.save(surface,'Green3.png')

def Green4():
    # Rectangles
    pygame.draw.rect(surface, GREEN, pygame.Rect(0,0,300,100),border_top_left_radius=50, border_top_right_radius=50, border_bottom_left_radius=50, border_bottom_right_radius=50)
    pygame.draw.rect(surface, GREEN, pygame.Rect(100,100,100,100),border_top_left_radius=-1, border_top_right_radius=-1, border_bottom_left_radius=50, border_bottom_right_radius=50)

    # Holes
    hole_list = [[(250,50),40],
                 [(150,150),40]]
    for hole in hole_list:
        pygame.draw.circle(surface, BLACK, hole[0],hole[1])

    # pygame.draw.polygon(surface, GRAY, polygon,width=10)
    pygame.image.save(surface,'Green4.png')

def Blue4():
    # Rectangles
    pygame.draw.rect(surface, BLUE, pygame.Rect(0,0,400,100),border_top_left_radius=50, border_top_right_radius=50, border_bottom_left_radius=50, border_bottom_right_radius=50)

    # Holes
    hole_list = [[(150,50),40]]
    for hole in hole_list:
        pygame.draw.circle(surface, BLACK, hole[0],hole[1])

    # pygame.draw.polygon(surface, GRAY, polygon,width=10)
    pygame.image.save(surface,'Blue4.png')

def Blue5():
    # Rectangles
    pygame.draw.rect(surface, BLUE, pygame.Rect(0,0,300,100),border_top_left_radius=50, border_top_right_radius=50, border_bottom_left_radius=50, border_bottom_right_radius=-1)
    pygame.draw.rect(surface, BLUE, pygame.Rect(100,100,200,100),border_top_left_radius=-1, border_top_right_radius=-1, border_bottom_left_radius=50, border_bottom_right_radius=50)
    # Holes
    hole_list = [[(150,150),40],
                 [(250,150),40]]
    for hole in hole_list:
        pygame.draw.circle(surface, BLACK, hole[0],hole[1])

    # pygame.draw.polygon(surface, GRAY, polygon,width=10)
    pygame.image.save(surface,'Blue5.png')

def Yellow3():
    # Rectangles
    pygame.draw.rect(surface, YELLOW, pygame.Rect(0,0,300,100),border_top_left_radius=50, border_top_right_radius=50, border_bottom_left_radius=50, border_bottom_right_radius=50)

    # Holes
    hole_list = [[(50,50),40]]
    for hole in hole_list:
        pygame.draw.circle(surface, BLACK, hole[0],hole[1])

    # pygame.draw.polygon(surface, GRAY, polygon,width=10)
    pygame.image.save(surface,'Yellow3.png')

def Yellow5():
    # Rectangles
    pygame.draw.rect(surface, YELLOW, pygame.Rect(0,0,200,100),border_top_left_radius=50, border_top_right_radius=50, border_bottom_left_radius=50, border_bottom_right_radius=0)
    pygame.draw.rect(surface, YELLOW, pygame.Rect(100,100,200,100),border_top_left_radius=0, border_top_right_radius=50, border_bottom_left_radius=0, border_bottom_right_radius=50)
    pygame.draw.rect(surface, YELLOW, pygame.Rect(100,200,100,100),border_top_left_radius=0, border_top_right_radius=0, border_bottom_left_radius=50, border_bottom_right_radius=50)

    # Holes
    hole_list = [[(50,50),40],
                 [(150,50),40],
                 [(250,150),40]]
    for hole in hole_list:
        pygame.draw.circle(surface, BLACK, hole[0],hole[1])

    # pygame.draw.polygon(surface, GRAY, polygon,width=10)
    pygame.image.save(surface,'Yellow5.png')

def Pin():
    pygame.draw.circle(surface, RED, (50,50),35)
    pygame.image.save(surface,'RedPin.png')


if __name__ == '__main__':
    pygame.init()
    surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Pin()

    while True:
        # Quitting the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # Update the display
        pygame.display.update()