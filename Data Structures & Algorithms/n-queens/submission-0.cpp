class Solution {
public:
    bool underAttack(vector<string>& board, int n, int x, int y) {
        for(int i=1; i<n; i++) {
            if(y-i<0) break;
            if(board[y-i][x]=='Q') return true;
            if(x-i>=0 && board[y-i][x-i]=='Q') return true;
            if(x+i<n && board[y-i][x+i]=='Q') return true;
        }
        return false;
    }
    vector<vector<string>> recursive(vector<string> curr_board, int n, int col)
    {
        if(col>=n) return {curr_board};
        vector<vector<string>> res;
        for(int i=0; i<n; i++) {
            if(!underAttack(curr_board,n,i,col)) {
                auto newBoard = curr_board;
                newBoard[col][i]='Q';
                auto newRes = recursive(newBoard,n,col+1);
                res.insert(res.end(),newRes.begin(),newRes.end());
            }
        }
        return res;
    }

    vector<vector<string>> solveNQueens(int n) {
        string all_stars = "";
        for(int i=0; i<n; i++) all_stars+='.';
        vector<string> emptyBoard(n, all_stars);

        return recursive(emptyBoard,n,0);        
    }
};
