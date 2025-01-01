import pygame,time
from Pieces import Board,Piece,RedL,RedZ,Blue4,Blue5,Green3,Green4,Yellow3,Yellow5,pieceGenerator
from parameters import HEIGHT,WIDTH
import GUI_Pieces
from GUI_Pieces import SURFACE_HEIGHT,SURFACE_WIDTH,WHITE,guiPieceGenerator,MainSurface

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
    mainSurface = MainSurface(50,50)

    for sol in solution:
        pieceType = sol[1]
        rot = sol[2]
        topleft = sol[3]

        shift = 0
        for block in pieceGenerator(pieceType,rot).shape[0]:
            if block == '':
                shift += 1
            else:
                break
        startingPos = (topleft[0],topleft[1]-shift)
        mainSurface.addPiece(pieceType,rot,startingPos)

    for pin in board.pin_list:
        colorDict = {'R':'RedPin','G':'GreenPin','B':'BluePin','Y':'YellowPin'}
        pieceType = colorDict[pin[0]]
        dict = {'A':0,'B':1,'C':2,'D':3}
        row = dict[pin[2]]
        col = int(pin[1]) - 1
        mainSurface.addPin(pieceType,(row,col))

    mainSurface.display()
    


def recursiveSolver(piecetype_list:list[Piece]):
    '''
    ### Recursively solves the puzzle.
    Tries to put the last piece to the top left position trying all rotations. If it doesn't succeed it returns 0.
    If a piece can be inserted, it logs the position and the rotation in the 'solution' list.
    '''
    topleft = emptyTopLeft()
    for newPieceType in piecetype_list:
        for rot in range(numberOfRotations(newPieceType)):
            newPiece = pieceGenerator(newPieceType,rot)
            id = 8 - len(piecetype_list)
            if board.addPiece(id,newPiece,topleft):
                solution.append([id,newPieceType,rot,topleft])
                new_piecetype_list = piecetype_list.copy()
                new_piecetype_list.remove(newPieceType)
                if new_piecetype_list == []:
                    # Puzzle is solved
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
                        solution.remove([id,newPieceType,rot,topleft])
                        board.removePiece(id)
            # Couldn't insert piece -> try the next rotation.
        # None of the rotations have suceeded -> try another piece
    # No combination was correct
    return False

def solve(exerciseSetup_pieces:list,exerciseSetup_pins:list[str]):
    '''
    ### Solves the puzzle with the given pieces and pins.
    exercise_pieces: [pieceType:str, rot:int, topleft:(row,col)]
    '''
    COMPLETE_PIECETYPE_LIST = ['RedL','RedZ','Green3','Green4','Blue4','Blue5','Yellow3','Yellow5']
    global board,solution
    board = Board(exerciseSetup_pins)
    solution = []
    for id,piece in enumerate(exerciseSetup_pieces):
        pieceType = piece[0]
        rot = piece[1]
        topleft = piece[2]
        solution.append([id,pieceType,rot,topleft])
        if not board.addPiece(id,pieceGenerator(pieceType,rot),topleft):
            print('Invalid setup.')
            return
        
    print('\n[Initial setup]')
    print(board)
    
    piecetype_list = [x for x in COMPLETE_PIECETYPE_LIST if x not in [ex_piece[0] for ex_piece in exerciseSetup_pieces]]

    if recursiveSolver(piecetype_list):
        print('Solution found!\n')
        print(board)
        displaySolution()
        return True
    else:
        print('No solution found.\n')
        return False

if __name__ == '__main__':
    # CHANGE THE EXERCISE SETUP HERE
    exerciseSetup_pins = ['R6B','G3C','B2B','B1C','Y4B','Y5C']
    exerciseSetup_pieces = [['Green4',6,(2,3)]]

    solve(exerciseSetup_pieces,exerciseSetup_pins)