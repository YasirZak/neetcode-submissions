class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m,n=len(board),len(board[0])
        def mark(i,j):
            if i<0 or i>=m or j<0 or j>=n or board[i][j]!="O":
                return

            board[i][j]="#"
            for di,dj in [(1,0),(0,1),(-1,0),(0,-1)]:
                mark(i+di,j+dj)


        for i in range(m):
            if board[i][0]=="O":
                mark(i,0)
            if board[i][n-1]=="O":
                mark(i,n-1)

        for j in range(n):
            if board[0][j]=="O":
                mark(0,j)
            if board[m-1][j]=="O":
                mark(m-1,j)

        for i in range(m):
            for j in range(n):
                if board[i][j]=="O":
                    board[i][j]="X"
                elif board[i][j]=="#":
                    board[i][j]="O"