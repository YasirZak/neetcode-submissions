class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int,int> counts;

        for(int num : nums) {
            if(counts.contains(num)) return true;
            counts[num]=1;
        }

        return false;
    }
};