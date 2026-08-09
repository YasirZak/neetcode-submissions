class Solution {
public:
    void helper(vector<vector<int>>& matrix, pair<int,int>& index) {
        int i = index.first;
        int j = index.second;
        
        for(int h=i; h<matrix.size(); h++) {
            matrix[h][j]=0;
        }

        for(int h=i; h>=0; h--) {
            matrix[h][j]=0;
        }

        for(int v=j; v<matrix[0].size(); v++) {
            matrix[i][v]=0;
        }

        for(int v=j; v>=0; v--) {
            matrix[i][v]=0;
        }
    }

    void setZeroes(vector<vector<int>>& matrix) {
        vector<pair<int,int>> indexes;

        for(int i=0; i<matrix.size(); i++) {
            for(int j=0; j<matrix[0].size(); j++) {
                if(matrix[i][j]==0) {
                    indexes.push_back({i,j});
                }
            }
        }

        for(auto p : indexes) {
            helper(matrix,p);
        }
    }
};
