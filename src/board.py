"""
Start by defining a board class. 

Key parameters:
    1. Board Size - 7
    2. Number of Pieces per Player
    3. Where the pieces are on which part of the board

"""



class Board: 
    def __init__(self, size=7):
        self.size = size
        self.grid = [
            [None for _ in range(self.size)]
            for _ in range(self.size)
        ]
    
    def get(self,row,col):
        return self.grid[row][col]










