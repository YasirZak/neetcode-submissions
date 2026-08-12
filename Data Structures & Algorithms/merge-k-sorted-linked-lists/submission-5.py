# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = None
        curNode = None
        heap = []
        counter=0

        for i in lists:
            heapq.heappush(heap, (i.val,counter,i))
            counter+=1

        while heap:
            _,_,i = heapq.heappop(heap)

            if head is None:
                head = i
                curNode = i
            else:
                curNode.next = i
                curNode = curNode.next
                
            i = i.next
            if i is not None:
                heapq.heappush(heap,(i.val,counter,i))
            counter+=1

        return head


