class Solution:

    def if_not_exists(self,board,x1, x2, y1, y2, num):
        for i in range(x1-1, x2):
            for j in range(y1-1, y2):
                if board[i][j] == str(num):
                    return False
        return True
    
    def check_in_grid(self,board,x, y,num):
        if x >= 1 and x <= 3:
            if y >= 1 and y <= 3:
                return self.if_not_exists(board, 1, 3, 1,3, num)
            if y >= 4  and y <= 6:
                return self.if_not_exists(board, 1,3,4, 6, num)
            if y >= 7 and y <= 9:
                return self.if_not_exists(board, 1,3,7, 9, num)
            
        if x >= 4 and x <= 6:
            if y >= 1 and y <= 3:
                return self.if_not_exists(board, 4,6,1, 3, num)
            if y >= 4  and y <= 6:
                return self.if_not_exists(board, 4,6, 4,6, num)
            if y >= 7 and y <= 9:
                return self.if_not_exists(board, 4,6,7, 9, num)
        
        if x >= 7 and x <= 9:
            if y >= 1 and y <= 3:
                return self.if_not_exists(board, 7,9,1, 3, num)
            if y >= 4  and y <= 6:
                return self.if_not_exists(board, 7,9,4, 6, num)
            if y >= 7 and y <= 9:
                return self.if_not_exists(board, 7,9,7, 9, num)
            
    def check_in_column(self, board, x, y,num):
        return self.if_not_exists(board, x, x, 1, 9, num)

    def check_in_row(self, board, x, y,num):
        return self.if_not_exists(board,1, 9, y, y, num)
    
    def isValid(self, board, x, y, num):
        return bool(self.check_in_column(board,x,y,num) and self.check_in_grid(board,x,y,num) and self.check_in_row(board,x,y,num))

    def recurse_solve(self, board):
        for row in range(1,10):
            for col in range(1,10):
                if board[row-1][col-1] == ".":
                    for element in range(1,10):
                        if self.isValid(board, row, col, element):
                            board[row-1][col-1] = str(element)
                            if self.recurse_solve(board):
                                return True
                            else:
                                board[row-1][col-1] = "."
                    return False
        return True



    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.recurse_solve(board)
        
