import pygame,time
from Pieces import HEIGHT,WIDTH,Board,Piece,RedL,RedZ,Blue4,Blue5,Green3,Green4,Yellow3,Yellow5
import GUI_Pieces
from GUI_Pieces import SCREEN_HEIGHT,SCREEN_WIDTH,guiPieceGenerator

'''
solution = {rL:[(0,0),1],
            rZ:[(0,0),1],
            g3:[(0,0),1]}
'''

def emptyTopLeft():
        '''Returns the top left corner that is still empty.'''
        for row in range(HEIGHT):
            for col in range(WIDTH):
                if board.grid[row][col] == '.':
                    return (row,col)
                
def printSolutionList():
    print('------ Solution ------ ')
    for sol in solution:
        print(f'({sol[0]}) {pieceGenerator(sol[1],sol[3]).__class__.__name__} {sol[2]} rot={sol[3]}')
    print('----------------------')

def printPieceTypeList(piecetype_list):
    print('piecetype_list: ',end='[')
    for idx,piecetype in enumerate(piecetype_list):
        if idx == len(piecetype_list) - 1:
            print(pieceGenerator(piecetype,0).__class__.__name__,end=']\n')
        else:
            print(pieceGenerator(piecetype,0).__class__.__name__,end=', ')

def pieceGenerator(pieceType:int,rot:int):
    match pieceType:
        case 0:
            return RedL(rot)
        case 1:
            return RedZ(rot)
        case 2:
            return Green3(rot)
        case 3:
            return Green4(rot)
        case 4:
            return Blue4(rot)
        case 5:
            return Blue5(rot)
        case 6:
            return Yellow3(rot)
        case 7:
            return Yellow5(rot)
        
def numberOfRotations(pieceType):
    if pieceType == 4 or pieceType == 6:
        return 4
    else:
        return 8
    
def displaySolution():
    pygame.init()
    surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
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
    # printPieceTypeList(piecetype_list)
    # printSolutionList()
    # print(board)
    # displaySolution()
    topleft = emptyTopLeft()
    # print(emptyTopLeft())
    for newPieceType in piecetype_list:
        # print(f'>>{pieceGenerator(newPieceType,0).__class__.__name__}')
        for rot in range(numberOfRotations(newPieceType)):
            # print(f'rot={rot}')
            newPiece = pieceGenerator(newPieceType,rot)
            id = 8 - len(piecetype_list)
            if board.insertPiece(id,newPiece,topleft):
                # piecetype_list.remove(newPieceType)
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
                        # printPieceTypeList(piecetype_list)
            # Couldn't insert piece -> try the next rotation.
        # None of the rotations have suceeded -> try another piece
    # No combination was correct
    # print('Returning False.')
    return False



if __name__ == '__main__':
    solution = []
    board = Board(['Y6B'])
    piecetype_list = [0,1,2,3,4,5,6,7]
    recursiveSolver(piecetype_list)
    print(board)
    printSolutionList()
    displaySolution()