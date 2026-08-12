class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            check = set()
            for j in range(9):
                if board[i][j]==".":
                    continue
                if board[i][j]<"1" or board[i][j]>"9" or (board[i][j] in check):
                    # print("1")
                    return False
                check.add(board[i][j])

        for j in range(9):
            check = set()
            for i in range(9):
                if board[i][j] == ".":
                    continue 
                if board[i][j] in check:
                    # print(2)
                    return False
                check.add(board[i][j])

        for si in range(0,9,3):
            for sj in range(0,9,3):
                check = set()
                for i in range(3):
                    for j in range(3):
                        if board[si+i][sj+j] == ".":
                            continue 
                        if board[si+i][sj+j] in check:
                            # print(3)
                            return False
                        check.add(board[si+i][sj+j])

        return True