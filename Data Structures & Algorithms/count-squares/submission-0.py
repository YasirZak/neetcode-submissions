class CountSquares:

    def __init__(self):
        self.xs = {}

    def add(self, point: List[int]) -> None:
        x,y = point
        if x not in self.xs:
            self.xs[x]={}
        if y not in self.xs[x]:
            self.xs[x][y]=0

        self.xs[x][y]+=1

    def count(self, point: List[int]) -> int:
        x,y=point
        if x not in self.xs: return 0

        res=0
        for xi in self.xs.keys():
            if xi==x: continue
            if y not in self.xs[xi]: continue
            side = xi-x
            if y+side in self.xs[x] and y+side in self.xs[xi]:
                res+= self.xs[x][y+side]*self.xs[xi][y]*self.xs[xi][y+side]
            if y-side in self.xs[x] and y-side in self.xs[xi]:
                res+= self.xs[x][y-side]*self.xs[xi][y]*self.xs[xi][y-side]

        return res
