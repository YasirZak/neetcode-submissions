class Solution {
public:
    vector<int> lookup;
    int recRob(vector<int>& nums, int i) {
        if(i>=nums.size()) return 0;
        if(lookup[i]==-1) lookup[i] = max(nums[i]+recRob(nums,i+2), recRob(nums,i+1));
        return lookup[i];
    }

    int rob(vector<int>& nums) {
        lookup = vector<int>(nums.size(),-1);
        return recRob(nums,0);
    }
};