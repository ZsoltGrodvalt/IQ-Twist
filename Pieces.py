import copy

HEIGHT = 4
WIDTH = 8

EMPTY_GRID = [['.','.','.','.','.','.','.','.'],
              ['.','.','.','.','.','.','.','.'],
              ['.','.','.','.','.','.','.','.'],
              ['.','.','.','.','.','.','.','.']]

RED = 0
GREEN = 1
BLUE = 2
YELLOW = 3


class Board:
    def __init__(self,newPins):
        self.pins = copy.deepcopy(EMPTY_GRID)
        self.pin_list = []
        self.addPins(newPins)
        self.grid = copy.deepcopy(EMPTY_GRID)

    def __str__(self):
        string = '  >> Board <<         >> Pins <<\n'
        for i in range(HEIGHT):
            for j in range(WIDTH):
                string += str(self.grid[i][j]) + ' '
            string +='    '
            for j in range(WIDTH):
                string += str(self.pins[i][j]) + ' '
            string += '\n'
        return string

    def addPins(self,newPins:list[str]) -> None:
        """Adds the pins to the grid.

        Args:
            newPins (list[str]): list of pins, eg. ['R3A', 'R6C','B2B'] for 2 red and 1 blue pin.
        """
        for pin in newPins:
            # Add pins to pin_list
            self.pin_list.append(pin)
            
            # Add pins to grid
            colorDict = {'R':0,'G':1,'B':2,'Y':3}
            dict = {'A':0,'B':1,'C':2,'D':3}
            row = dict[pin[2]]
            col = int(pin[1]) - 1
            self.pins[row][col] = colorDict[pin[0]]

    def addPiece(self,id,pieceType:str,rotation:int,topLeft:tuple) -> bool:
        '''Adds the piece to the grid. Returns True if successful, False otherwise.'''
        piece = pieceGenerator(pieceType,rotation)
        if self.checkPotentialBlocks(piece,topLeft):
            self.insertPiece(id,piece,topLeft)
            return True
        return False

    def addPiece(self,id,piece,topLeft):
        """
        First checks whether the blocks are free, if yes, it inserts the piece and returns True.\\
        Returns False otherwise.\\
        Checks if the top left corner of the piece is not empty. If it is, it has to 'shift' the piece until the top left is 1/0.
        ### pos(row,col)
        """        
        shift = 0
        for block in piece.shape[0]:
            if block == '':
                shift += 1
            else:
                break
        # print(f'shift={shift}')
        shiftedTopLeft = (topLeft[0],topLeft[1]-shift)

        if self.checkPotentialBlocks(piece,shiftedTopLeft):
            self.insertPiece(id,piece,shiftedTopLeft)
            return True
        return False
        

    def checkPotentialBlocks(self,piece,topLeft):
        '''# Internal function.
        
        Checks whether the blocks where the new piece will be inserted are free and are in the grid.
        '''
        startingRow = topLeft[0]
        startingColumn = topLeft[1]
        if ((startingRow < 0) or (startingColumn < 0) or (startingRow + piece.ydim) > HEIGHT) or  ((startingColumn + piece.xdim) > WIDTH):
            # print(f'[LOG] Part of "{piece.__class__.__name__}" would be outside the grid.')
            return False
        
        # First check whether the positions are correct and the new piece would not clash with the ones that are already there.
        for rowIndex,row in enumerate(piece.shape):
            r = startingRow + rowIndex
            for columnIndex,block in enumerate(row):      # block is the certain part of the piece [1/0/'']
                c = startingColumn + columnIndex
                # If block is empty (depends on the shape of the piece), skip
                if block == '':
                    continue
                # If position is occupied (not '.'), return False.
                if self.grid[r][c] != '.':
                    # print(f'[LOG] "{piece.__class__.__name__}": Position is occupied.')
                    return False
                # If there is a pin, then the colour has to be right, and there must be a hole.
                if (self.pins[r][c] != '.') and (self.pins[r][c] != piece.color or block != 0):
                    # print(f'[LOG] "{piece.__class__.__name__}": No/Incorrect hole')
                    return False
        # If everything is correct, return True.
        # print('Insert block returns True.')
        return True

    def insertPiece(self,id,piece,startingPos):
        '''# Internal function.'''
        startingRow = startingPos[0]
        startingColumn = startingPos[1]
        for rowIndex,row in enumerate(piece.shape):
            for columnIndex,block in enumerate(row): 
                r = startingRow + rowIndex
                c = startingColumn + columnIndex
                # Overwrite the grid.
                if block != '':
                    self.grid[r][c] = id

    def removePiece(self,pieceNumber):
        '''Inserts '.' instead of 'pieceNumber'. '''
        for row in range(HEIGHT):
            for col in range(WIDTH):
                if self.grid[row][col] == pieceNumber:
                    self.grid[row][col] = '.'



class Piece:
    def __init__(self):
        self.xdim = len(self.shape[0])
        self.ydim = len(self.shape)

    def __str__(self):
        string = ''
        for row in self.shape:
            for block in row:
                if block != '':
                    string += str(block) + ' '
                else:
                    string += '  '
            string += '\n'
        return string

class RedL(Piece):
    def __init__(self,rotation):
        self.color = RED
        self.rotatePiece(rotation)
        self.maxRotation = 8
        super().__init__()

    def rotatePiece(self,rotation):
        match rotation:
            case 0:
                self.shape = [[0,1,0],[1,'','']]  
            case 1:
                self.shape = [[0,''],[1,''],[0,1]]  
            case 2:
                self.shape = [['','',1],[0,1,0]]
            case 3:
                self.shape = [[1,0],['',1],['',0]]  
            case 4:
                self.shape = [[0,1,0],['','',1]]
            case 5:
                self.shape = [[0,1],[1,''],[0,'']]  
            case 6:
                self.shape = [[1,'',''],[0,1,0]]
            case 7:
                self.shape = [['',0],['',1],[1,0]] 

class RedZ(Piece):
    def __init__(self,rotation):
        self.color = RED
        self.rotatePiece(rotation)
        self.maxRotation = 8
        super().__init__()

    def rotatePiece(self,rotation):
        match rotation:
            case 0:
                self.shape = [[1,1,''],['',0,1]]  
            case 1:
                self.shape = [['',1],[1,0],[1,'']]  
            case 2:
                self.shape = [[1,0,''],['',1,1]]
            case 3:
                self.shape = [['',1],[0,1],[1,'']] 
            case 4:
                self.shape = [['',1,1],[1,0,'']]
            case 5:
                self.shape = [[1,''],[1,0],['',1]]  
            case 6:
                self.shape = [['',0,1],[1,1,'']]
            case 7:
                self.shape = [[1,''],[0,1],['',1]]  

class Green3(Piece):
    def __init__(self,rotation):
        self.color = GREEN
        self.rotatePiece(rotation)
        self.maxRotation = 8
        super().__init__()

    def rotatePiece(self,rotation):
        match rotation:
            case 0:
                self.shape = [[0,0],['',1]]  
            case 1:
                self.shape = [[0,1],[0,'']]  
            case 2:
                self.shape = [[1,''],[0,0]]  
            case 3:
                self.shape = [['',0],[1,0]] 
            case 4:
                self.shape = [[0,0],[1,'']]  
            case 5:
                self.shape = [[0,''],[0,1]]  
            case 6:
                self.shape = [['',1],[0,0]]  
            case 7:
                self.shape = [[1,0],['',0]] 

class Green4(Piece):
    def __init__(self,rotation):
        self.color = GREEN
        self.rotatePiece(rotation)
        self.maxRotation = 8
        super().__init__()

    def rotatePiece(self,rotation):
        match rotation:
            case 0:
                self.shape = [[1,1,0],['',0,'']]  
            case 1:
                self.shape = [[0,''],[1,0],[1,'']]  
            case 2:
                self.shape = [['',0,''],[0,1,1]]
            case 3:
                self.shape =[['',1],[0,1],['',0]]  
            case 4:
                self.shape = [[0,1,1],['',0,'']] 
            case 5:
                self.shape = [[1,''],[1,0],[0,'']]   
            case 6:
                self.shape = [['',0,''],[1,1,0]]
            case 7:
                self.shape = [['',0],[0,1],['',1]]  

class Blue4(Piece):
    def __init__(self,rotation):
        self.color = BLUE
        self.rotatePiece(rotation)
        self.maxRotation = 4
        super().__init__()

    def rotatePiece(self,rotation):
        match rotation:
            case 0:
                self.shape = [[1,0,1,1]]        #[['1','0','1','1']]
            case 1:
                self.shape = [[1],[1],[0],[1]]  #[['1'],['1'],['0'],['1']]
            case 2:
                self.shape = [[1,1,0,1]]        #[['1','1','0','1']]
            case 3:
                self.shape = [[1],[0],[1],[1]]  #[['1'],['0'],['1'],['1']]

class Blue5(Piece):
    def __init__(self,rotation):
        self.color = BLUE
        self.rotatePiece(rotation)
        self.maxRotation = 8
        super().__init__()

    def rotatePiece(self,rotation):
        match rotation:
            case 0:
                self.shape = [[1,1,1],['',0,0]]   
            case 1:
                self.shape = [[1,0],[1,0],[1,'']] 
            case 2:
                self.shape = [[0,0,''],[1,1,1]]  
            case 3:
                self.shape = [['',1],[0,1],[0,1]] 
            case 4:
                self.shape = [[1,1,1],[0,0,'']] 
            case 5:
                self.shape = [[1,''],[1,0],[1,0]] 
            case 6:
                self.shape = [['',0,0,],[1,1,1]]  
            case 7:
                self.shape = [[0,1],[0,1],['',1]] 

class Yellow3(Piece):
    def __init__(self,rotation):
        self.color = YELLOW
        self.rotatePiece(rotation)
        self.maxRotation = 4
        super().__init__()

    def rotatePiece(self,rotation):
        match rotation:
            case 0:
                self.shape = [[0,1,1]]  
            case 1:
                self.shape = [[1],[1],[0]] 
            case 2:
                self.shape = [[1,1,0]] 
            case 3:
                self.shape = [[0],[1],[1]]

class Yellow5(Piece):
    def __init__(self,rotation):
        self.color = YELLOW
        self.rotatePiece(rotation)
        self.maxRotation = 8
        super().__init__()

    def rotatePiece(self,rotation):
        match rotation:
            case 0:
                self.shape = [[0,0,''],['',1,0],['',1,'']]  
            case 1:
                self.shape = [['',0,''],[0,1,1],[0,'','']] 
            case 2:
                self.shape = [['',1,''],[0,1,''],['',0,0]] 
            case 3:
                self.shape = [['','',0],[1,1,0],['',0,'']]
            case 4:
                self.shape = [['',0,0],[0,1,''],['',1,'']]  
            case 5:
                self.shape = [[0,'',''],[0,1,1],['',0,''],] 
            case 6:
                self.shape = [['',1,''],['',1,0],[0,0,'']] 
            case 7:
                self.shape = [['',0,''],[1,1,0],['','',0]]


def pieceGenerator(pieceType:str,rot:int):
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

if __name__ == '__main__':
    # board = Board(['B3A', 'R6C','B2B'])
    board = Board(['B2C','B8D'])
    # print(board)
    # print(Blue4(1))
    # board.insertPiece(0,Blue4(2),(0,0))
    # board.insertPiece(1,Blue4(0),(3,1))
    # board.removePiece(1)
    # print(board)
    piece = Yellow5(0)
    print(piece)
    board.addPiece(1,piece,(1,3))
    print(board)
    # board.addPins(['Y4C'])
    # print(board)

    # for i in range(8):
    #     print(f'Rotation: {i}')
    #     print(RedZ(i))
