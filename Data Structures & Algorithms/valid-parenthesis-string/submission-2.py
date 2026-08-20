class Solution:
    def checkValidString(self,s:str)->bool:
        p_stack = deque()
        s_stack = deque()

        for i,c in enumerate(s):
            if c=='*':
                s_stack.append(i)
            elif c=='(':
                p_stack.append(i)
            else:
                if p_stack:
                    p_stack.pop()
                else:
                    if not s_stack:
                        return False
                    s_stack.pop()

        while p_stack:
            if not s_stack:
                return False
            p_top, s_top = p_stack.pop(),s_stack.pop()
            if p_top>s_top:
                return False

        return True