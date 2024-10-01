#given N quuen , we have n x n chess board. 
#Goal is to place queens , and they cannot attack each other. 
# so in a row or in column or any diagonal , there should not be two queens.

class Solution:
    def solveNQueens(self, n:int) -> list[list[str]]:
        col = set()
        posDiag = set() # r+c
        negDiag = set()  # r-c

        res = []
        board = [["."] *n for i in range(n)]



        def backtrack(r):
            if r ==n:
                copy_board = ["".join (row) for row in board]
                res.append(copy_board)
                return
            
            for c  in range(n):
                if  c in col or (r+c) in posDiag or (r-c ) in negDiag:
                    continue  # pruning
                else:
                    col.add(c)
                    posDiag.add(r+c)
                    negDiag.add(r-c)
                    board[r][c] = "Q"


                    #move to next row
                    backtrack(r+1)



                    # remove the queen
                    col.remove(c)
                    posDiag.remove(r+c)
                    negDiag.remove(r-c)
                    board[r][c] = "."
        backtrack(0)
        

        return res
    


# Example usage
solution = Solution()
result = solution.solveNQueens(5)
for board in result:
    for row in board:
        print(row)
    print()  # To separate different solutions