import pygame
from pygame.transform import rotate, flip

SURFACE_WIDTH = 800
SURFACE_HEIGHT = 400
BLOCK_SIZE = 100

RED = (205,0,0)
GREEN = (50,205,50)
BLUE = (0,0,205)
YELLOW = (255,215,0)
BLACK = (0,0,0)
WHITE = (255, 255, 255)



class Piece:
    def __init__(self,rotation):
        self.img = pygame.image.load("images/" + self.__class__.__name__ +  ".png").convert()
        # print("'images/" + self.__class__.__name__ +  ".png' was loaded.")
        self.img.set_colorkey(BLACK) # Set the transparent colorkey

        if rotation < 4:
            self.img = rotate(self.img, rotation*90)
        else:
            self.img = flip(self.img, True,False)
            self.img = rotate(self.img, rotation*90)

def guiPieceGenerator(pieceType:int,rot:int):
    match pieceType:
        case 'RedL':
            return RedL(rot)
        case 'RedZ':
            return RedZ(rot)
        case 'Green3':
            return Green3(rot)
        case 'Green4':
            return Green4(rot)
        case 'Blue4':
            return Blue4(rot)
        case 'Blue5':
            return Blue5(rot)
        case 'Yellow3':
            return Yellow3(rot)
        case 'Yellow5':
            return Yellow5(rot)
        case 'RedPin':
            return RedPin(0)
        case 'GreenPin':
            return GreenPin(0)
        case 'BluePin':
            return BluePin(0)
        case 'YellowPin':
            return YellowPin(0)

class RedL(Piece):
    def __init__(self,rotation):
        super().__init__(rotation)

class RedZ(Piece):
    def __init__(self,rotation):
        super().__init__(rotation)
    
class Green3(Piece):
    def __init__(self,rotation):
        super().__init__(rotation)

class Green4(Piece):
    def __init__(self,rotation):
        super().__init__(rotation)

class Blue4(Piece):
    def __init__(self,rotation):
        super().__init__(rotation)

class Blue5(Piece):
    def __init__(self,rotation):
        super().__init__(rotation)

class Yellow3(Piece): 
    def __init__(self,rotation):
        super().__init__(rotation)

class Yellow5(Piece):
    def __init__(self,rotation):
        super().__init__(rotation)

class YellowPin(Piece):
    def __init__(self,rotation):
        super().__init__(rotation)

class BluePin(Piece):
    def __init__(self,rotation):
        super().__init__(rotation)

class RedPin(Piece):
    def __init__(self,rotation):
        super().__init__(rotation)

class GreenPin(Piece):
    def __init__(self,rotation):
        super().__init__(rotation)


if __name__ == '__main__':
    pygame.init()
    X_RIM = 50
    Y_RIM = 50
    GUI_WIDTH = SURFACE_WIDTH + X_RIM
    GUI_HEIGHT = SURFACE_HEIGHT + Y_RIM

    main_surface = pygame.display.set_mode((GUI_WIDTH, GUI_HEIGHT))
    surface = pygame.Surface((SURFACE_WIDTH, SURFACE_HEIGHT))
    pygame.display.set_caption("IQTwist")


    # Adds the img to the surface
    surface.blit(RedL(2).img,(500,200)) 
    surface.blit(RedZ(5).img,(200,0)) 
    surface.blit(Green3(0).img,(0,0)) 
    surface.blit(Green4(5).img,(400,100)) 
    surface.blit(Blue4(0).img,(300,0)) 
    surface.blit(Blue5(2).img,(100,200)) 
    surface.blit(Yellow3(3).img,(0,100)) 
    surface.blit(Yellow5(3).img,(500,0)) 

    surface.blit(YellowPin(0).img,(500,200)) 
    surface.blit(YellowPin(0).img,(100,200))
    surface.blit(BluePin(0).img,(0,0))  
    surface.blit(BluePin(0).img,(300,100))
    surface.blit(GreenPin(0).img,(700,300)) 
    surface.blit(GreenPin(0).img,(500,300))
    surface.blit(RedPin(0).img,(400,300))

    main_surface.blit(surface,(X_RIM,Y_RIM))
    font = pygame.font.SysFont('Arial', 50)
    
    for y in range(1,5):
        yletter = font.render(chr(64+y), True, WHITE)
        y_Rect = yletter.get_rect()
        y_Rect.center = (X_RIM//2, Y_RIM + 50 + 100*(y-1))
        main_surface.blit(yletter,y_Rect)

    for x in range(1,9):
        xletter = font.render(str(x), True, WHITE)
        x_Rect = xletter.get_rect()
        x_Rect.center = (X_RIM + 50 + 100*(x-1), Y_RIM//2)
        main_surface.blit(xletter,x_Rect)

    # Main loop
    while True:
        # Quitting the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # Update the display
        pygame.display.update()