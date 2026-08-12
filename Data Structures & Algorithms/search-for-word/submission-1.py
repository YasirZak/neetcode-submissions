class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def search(board,word,visited,i,j,k):
            if k>=len(word): 
                return True

            if i<0 or j<0 or i>=len(board) or j>=len(board[0]) or (i,j) in visited:
                return False

            if board[i][j]!=word[k]:
                return False

            visited.add((i,j))

            res = False
            for di,dj in [(1,0), (0,1), (-1,0), (0,-1)]:
                res = res or search(board,word,visited,i+di,j+dj,k+1)

            visited.remove((i,j))

            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                v = set()
                if search(board,word,v,i,j,0):
                    return True

        return False