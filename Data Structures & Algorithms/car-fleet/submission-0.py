class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        comb = sorted([(position[i],speed[i]) for i in range(len(speed))], reverse=True)

        stk = []
        for pos,spd in comb:
            time = (target-pos)/spd
            if not stk:
                stk.append(time)
            else:
                if stk[-1]<time:
                    stk.append(time)

        return len(stk)    