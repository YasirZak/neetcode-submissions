class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}
        def helper(s,wd):
            if s=="": return True
            if s in dp: return dp[s]

            for i in range(len(s)+1):
                if s[0:i] in wd:
                    if helper(s[i:],wd):
                        dp[s]=True
                        return True

            dp[s]=False
            return False

        wordDict = set(wordDict)
        return helper(s,wordDict)