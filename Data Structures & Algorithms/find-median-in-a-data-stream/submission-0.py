class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        if len(self.arr)==0:
            self.arr.append(num)
            # print(self.arr)
            return

        s=0
        e=len(self.arr)-1

        while s<e:
            m=(s+e)//2
            if num==self.arr[m]:
                s=m
                break
            elif num<self.arr[m]:
                e=m-1
            else:
                s=m+1

        if num<=self.arr[s]:
            self.arr.insert(s,num)
        else:
            self.arr.insert(s+1,num)

        # print(self.arr)

    def findMedian(self) -> float:
        n = len(self.arr)
        if n%2==1:
            return self.arr[(n-1)//2]
        return (self.arr[n//2]+self.arr[(n-1)//2])/2
        
        
        