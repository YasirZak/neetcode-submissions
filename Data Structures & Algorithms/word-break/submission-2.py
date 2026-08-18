class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        i=0
        min_len = min([len(word) for word in wordDict])
        for j in range(len(s)+1):
            if s[i:j] in wordDict and (len(s)-j==0 or len(s)-j>=min_len):
                i=j

        if i==len(s): return True

        i=len(s)
        for j in range(len(s)-1,-1,-1):
            if s[j:i] in wordDict and (j==0 or j>=min_len):
                i=j

        return i==0