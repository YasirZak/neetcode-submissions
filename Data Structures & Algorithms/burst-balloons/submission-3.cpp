class Solution {
public:
    int recurse(vector<int>& nums, int l, int r, vector<vector<int>>& dp) {
        if(l>r) return 0;
        if(dp[l][r]!=-1) return dp[l][r];
        for(int i=l; i<=r; i++) {
            int prev = recurse(nums,l,i-1,dp);
            int nxt = recurse(nums,i+1,r,dp);
            dp[l][r] = max(dp[l][r],
            nums[l-1]*nums[i]*nums[r+1]+prev+nxt);
        }
        return dp[l][r];
    }

    int maxCoins(vector<int>& nums) {
        int n=nums.size();
        vector<int>newNums(n+2,1);
        for(int i=0; i<n; i++) newNums[i+1]=nums[i];
        vector<vector<int>> dp(n+2,vector<int>(n+2,-1));
        return recurse(newNums,1,n,dp);
    }
};
