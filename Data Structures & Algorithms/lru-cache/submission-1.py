class Node:
    def __init__(self,key:int,val:int,prev:Optional[Node]=None,next:Optional[Node]=None):
        self.key=key
        self.val=val
        self.prev=prev
        self.next=next

class LRUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.n=0
        self.h, self.t = None,None
        self.m = {}
        
    def add(self,node):
        if not node: return
        if not self.t:
            self.h=node
            self.t=node
            return
        self.t.next=node
        node.prev = self.t
        self.t=self.t.next

    def remove(self,node):
        if not node: return
        if node==self.h:
            if self.h: self.h=self.h.next
        if node==self.t:
            if self.t: self.t=self.t.prev
        prev=node.prev
        nxt=node.next
        node.prev=None
        node.next=None
        if prev: prev.next=nxt
        if nxt: nxt.prev=prev

    def get(self, key: int) -> int:
        if key not in self.m: return -1
        node=self.m[key]
        self.remove(node)
        self.add(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.m:
            node=self.m[key]
            node.val=value
            self.remove(node)
            self.add(node)
            return
        node=Node(key,value)
        self.m[key]=node
        self.add(node)
        self.n+=1

        if self.n>self.cap:
            hk = self.h.key
            self.remove(self.h)
            del self.m[hk]
            self.n-=1