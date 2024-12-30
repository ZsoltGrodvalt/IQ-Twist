import pygame,time
from Pieces import HEIGHT,WIDTH,Board,Piece,RedL,RedZ,Blue4,Blue5,Green3,Green4,Yellow3,Yellow5,pieceGenerator
import GUI_Pieces
from GUI_Pieces import SURFACE_HEIGHT,SURFACE_WIDTH,WHITE,guiPieceGenerator

def emptyTopLeft():
        '''Returns the top left corner that is still empty.'''
        for row in range(HEIGHT):
            for col in range(WIDTH):
                if board.grid[row][col] == '.':
                    return (row,col)
                
def printSolutionList():
    print('------ Solution ------ ')
    for sol in solution:
        id = sol[0]
        pieceType = sol[1]
        pos = sol[2]
        rot = sol[3]
        print(f'({id}) {pieceType} pos={pos} rot={rot}')
    print('----------------------')
        
def numberOfRotations(pieceType):
    """
    Returns the number of possible rotations for a given piece type.
    """
    if pieceType in ['Yellow3','Blue4']:
        return 4
    else:
        return 8
    
def displaySolution():
    pygame.init()
    X_RIM = 50
    Y_RIM = 50
    GUI_WIDTH = SURFACE_WIDTH + X_RIM
    GUI_HEIGHT = SURFACE_HEIGHT + Y_RIM

    main_surface = pygame.display.set_mode((GUI_WIDTH, GUI_HEIGHT))
    surface = pygame.Surface((SURFACE_WIDTH, SURFACE_HEIGHT))
    pygame.display.set_caption("IQTwist")

    for sol in solution:
        # [id,newPieceType,topleft,rot]
        pieceType = sol[1]
        topleft = sol[2]
        rot = sol[3]

        shift = 0
        for block in pieceGenerator(pieceType,rot).shape[0]:
            if block == '':
                shift += 1
        startingPos = (topleft[0],topleft[1]-shift)
        surface.blit(guiPieceGenerator(pieceType,rot).img,(startingPos[1]*100,startingPos[0]*100))
        # surface.blit(RedL(sol[3]).img,(500,200))

    for pin in board.pin_list:
        colorDict = {'R':10,'G':11,'B':12,'Y':13}
        pieceType = colorDict[pin[0]]
        dict = {'A':0,'B':1,'C':2,'D':3}
        row = dict[pin[2]]
        col = int(pin[1]) - 1
        surface.blit(guiPieceGenerator(pieceType,0).img,(col*100,row*100))

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
    while True:
        # Quitting the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # Update the display
        pygame.display.update()
    


def recursiveSolver(piecetype_list:list[Piece]):
    '''
    ### Recursively solves the puzzle.
    Tries to put the last piece to the top left position trying all rotations. If it doesn't succeed it returns 0.
    If a piece can be inserted, it logs the position and the rotation in the 'solution' list.
    '''
    # print(piecetype_list)
    # printSolutionList()
    # print(board)
    # displaySolution()
    topleft = emptyTopLeft()
    # print(emptyTopLeft())
    for newPieceType in piecetype_list:
        # print(f'>>{newPieceType}')
        for rot in range(numberOfRotations(newPieceType)):
            # print(f'rot={rot}')
            newPiece = pieceGenerator(newPieceType,rot)
            id = 8 - len(piecetype_list)
            if board.insertPiece(id,newPiece,topleft):
                solution.append([id,newPieceType,topleft,rot])
                new_piecetype_list = piecetype_list.copy()
                new_piecetype_list.remove(newPieceType)
                if new_piecetype_list == []:
                    # Puzzle is solved
                    print('Puzzle is solved!')
                    return True
                else:
                    # Continue with the next piece in the list.
                    # A new list is created, so nothing has to be removed from the original, 
                    # so if the recursion doesn't succeed, nothing has to be removed and then added again.
                    if recursiveSolver(new_piecetype_list):
                        # The following pieces led to the solution.
                        return True
                    else:
                        # recursion returned FALSE -> another rotation or piece has to be tried in this position.
                        solution.remove([id,newPieceType,topleft,rot])
                        board.removePiece(id)  # (UN)COMMENT THIS to see the first fill
                        # print(piecetype_list)
            # Couldn't insert piece -> try the next rotation.
        # None of the rotations have suceeded -> try another piece
    # No combination was correct
    # print('Returning False.')
    return False


if __name__ == '__main__':
    solution = []
    board = Board([])
    piecetype_list = ['RedL','RedZ','Green3','Green4','Blue4','Blue5','Yellow3','Yellow5']
    recursiveSolver(piecetype_list)
    print(board)
    printSolutionList()
    displaySolution()