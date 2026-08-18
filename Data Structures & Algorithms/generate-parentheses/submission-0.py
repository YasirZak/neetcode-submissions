class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def helper(o,c):
            if o==0:
                return [")"*c if c else ""]

            res1 = ["("+i for i in helper(o-1,c)]
            if o<c:
                res2=[")"+i for i in helper(o,c-1)]
            else: res2=[]

            return res1+res2

        return helper(n,n)