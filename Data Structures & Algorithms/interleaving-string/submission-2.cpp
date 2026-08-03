class Solution {
public:
    bool isInterleave(string s1, string s2, string s3) {
        int i=0, a=0, b=0, n1=0, n2=0;
        bool res1 = true;

        while(i<s3.length()) {
            if(s1[a] == s3[i]) {
                n1++;
                while(a<s1.length() && s1[a]==s3[i]) {
                    a++; i++;
                }
            }
            else if(s2[b] == s3[i]) {
                n2++;
                while(b<s2.length() && s2[b]==s3[i]) {
                    b++; i++;
                }
            } 
            else {
                res1 = false;
                break;
            };
        }

        if (res1)
        res1 = !(a<s1.length()) && !(b<s2.length()) && n1-n2>=-1 && n1-n2<=1;

        i=0; a=0; b=0; n1=0; n2=0;
        bool res2 = true;
        
        while(i<s3.length()) {
            if(s2[b] == s3[i]) {
                n2++;
                while(b<s2.length() && s2[b]==s3[i]) {
                    b++; i++;
                }
            }
            else if(s1[a] == s3[i]) {
                n1++;
                while(a<s1.length() && s1[a]==s3[i]) {
                    a++; i++;
                }
            } 
            else {
                res2 = false;
                break;
            };
        }

        if (res2)
        res2 = !(a<s1.length()) && !(b<s2.length()) && n1-n2>=-1 && n1-n2<=1;

        return res1 || res2;
    }
};
