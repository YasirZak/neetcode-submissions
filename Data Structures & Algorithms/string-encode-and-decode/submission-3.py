class Solution:

    def encode(self, strs: List[str]) -> str:
        split="|!@#$|"
        res=""
        for s in strs:
            res+=s+split
        return res

    def decode(self, s: str) -> List[str]:
        split="|!@#$|"
        return s.split(split)[:-1]
