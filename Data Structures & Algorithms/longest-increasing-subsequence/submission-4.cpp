class Solution {
public:

    int lengthOfLIS(vector<int>& nums) {
        int n = nums.size();
        vector<int> les(n,1);

        for(int i=1; i<n; i++) {
            for(int j=0; j<i; j++) {
                if(nums[i] > nums[j]) {
                    les[i] = max(les[i], les[j]+1);
                }
            }
        }

        return *max_element(les.begin(), les.end());
    }
};
