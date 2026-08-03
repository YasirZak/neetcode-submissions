class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        map<char,char> corr = {
            {')', '('},
            {']', '['},
            {'}', '{'}
        };

        for(char c : s) {
            if(c=='(' || c=='[' || c=='{') st.push(c);
            else if(st.empty() || st.top() != corr[c]) return false;
            else st.pop();
        }

        return st.empty();
    }
};
