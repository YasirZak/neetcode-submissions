class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        vector<vector<int>> res;
        vector<int> current=nums;
        res.push_back(current);
        while(next_permutation(nums.begin(),nums.end())) {
            current = nums;
            res.push_back(current);
        }

        return res;
    }
};
