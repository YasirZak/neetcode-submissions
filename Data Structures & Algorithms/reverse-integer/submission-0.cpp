class Solution {
public:
    int reverse(int x) {
        int res=0;
        bool neg = x<0;
        x = neg? -x : x;
        while(x!=0) {
            if(res>(INT_MAX-x%10)/10) return 0;
            res = res*10 + x%10;
            x /= 10;
        }
        return neg?-res:res;
    }
};
