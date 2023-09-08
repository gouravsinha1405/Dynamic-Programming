class Solution:
    def __init__(self,):
        self.output = []

    def isGridValid(self, queen_pos, current_pos):
        flag  = bool((queen_pos[0] == current_pos[0]) or 
                     (queen_pos[1] == current_pos[1]) or 
                     (abs(queen_pos[0]-current_pos[0]) == abs(queen_pos[1]-current_pos[1])))
        return not flag

    def solve(self, N, board, row, past_queen_pos):
        if row > N:
            res = ["".join(queen) for queen in board]
            self.output.append(res)
            return
        for col in range(1, N+1):
            if board[row-1][col-1] == ".":
                check_if_grid_valid = True
                for pos in past_queen_pos:
                    check_if_grid_valid *= self.isGridValid(pos, (row,col))
                if bool(check_if_grid_valid) or len(past_queen_pos) == 0:
                    board[row-1][col-1] = "Q"
                    past_queen_pos.add((row, col))
                    self.solve(N, board, row+1,past_queen_pos)
                    board[row-1][col-1] = "."
                    past_queen_pos.remove((row,col))
        return 

    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for _ in range(n)] for _ in range(n)]
        past_queen_pos = set()
        row = 1
        self.solve(n, board, row, past_queen_pos)
        return self.output

        
