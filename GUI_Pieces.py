import pygame
from pygame.transform import rotate, flip
from parameters import *

class Piece:
    def __init__(self,rotation):
        self.img = pygame.image.load("images/" + self.__class__.__name__ +  ".png").convert()
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

class MainSurface:
    def __init__(self,X_RIM=DEFAULT_X_RIM,Y_RIM=DEFAULT_Y_RIM):
        pygame.init()
        self.X_RIM = X_RIM
        self.Y_RIM = Y_RIM
        self.main_surface = pygame.display.set_mode((SURFACE_WIDTH+X_RIM, SURFACE_HEIGHT+Y_RIM))
        self.surface = pygame.Surface((SURFACE_WIDTH, SURFACE_HEIGHT))
        pygame.display.set_caption("IQ Twist")

    def addPiece(self,pieceType:str,rotation:int,pos:tuple):
        '''### pos(row,col)'''
        self.surface.blit(guiPieceGenerator(pieceType,rotation).img,(pos[1]*BLOCK_SIZE,pos[0]*BLOCK_SIZE))

    def addPin(self,pinType:str,pos:tuple):
        self.surface.blit(guiPieceGenerator(pinType,0).img,(pos[1]*BLOCK_SIZE,pos[0]*BLOCK_SIZE))

    def display(self):
        self.main_surface.blit(self.surface,(self.X_RIM,self.Y_RIM))
        font = pygame.font.SysFont('Arial', 50)
        
        for y in range(1,5):
            yletter = font.render(chr(64+y), True, WHITE)
            y_Rect = yletter.get_rect()
            y_Rect.center = (self.X_RIM//2, self.Y_RIM + BLOCK_SIZE/2 + BLOCK_SIZE*(y-1))
            self.main_surface.blit(yletter,y_Rect)

        for x in range(1,9):
            xletter = font.render(str(x), True, WHITE)
            x_Rect = xletter.get_rect()
            x_Rect.center = (self.X_RIM + BLOCK_SIZE/2 + BLOCK_SIZE*(x-1), self.Y_RIM//2)
            self.main_surface.blit(xletter,x_Rect)

        # Main loop
        while True:
            # Quitting the game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            # Update the display
            pygame.display.update() 

if __name__ == '__main__':
    mainSurface = MainSurface()
    mainSurface.addPiece('RedL',2,(2,5))
    mainSurface.addPiece('RedZ',5,(0,2))
    mainSurface.addPiece('Green3',0,(0,0))
    mainSurface.addPiece('Green4',5,(1,4))
    mainSurface.addPiece('Blue4',0,(0,3))
    mainSurface.addPiece('Blue5',2,(2,1))
    mainSurface.addPiece('Yellow3',3,(1,0))
    mainSurface.addPiece('Yellow5',3,(0,5))
    mainSurface.addPin('YellowPin',(2,5))
    mainSurface.addPin('YellowPin',(2,1))
    mainSurface.addPin('BluePin',(0,0))
    mainSurface.addPin('BluePin',(1,3))
    mainSurface.addPin('GreenPin',(3,7))
    mainSurface.addPin('GreenPin',(3,5))
    mainSurface.addPin('RedPin',(3,4))

    mainSurface.display()