class TimeMap:

    def __init__(self):
        self.m = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.m:
            self.m[key] = []
        self.m[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.m: return ""
        if self.m[key][0][0]>timestamp: return ""
        i,j = 0,len(self.m[key])-1
        while i<j:
            if j-i==1:
                if self.m[key][j][0]<=timestamp:
                    return self.m[key][j][1]
                else:
                    return self.m[key][i][1]
            mid = (i+j)//2
            if self.m[key][mid][0]==timestamp:
                return self.m[key][mid][1]
            elif self.m[key][mid][0]<timestamp:
                i=mid
            else:
                j=mid

        return self.m[key][i][1]
