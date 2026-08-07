# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head.next is None: return
        if head.next.next is None: return
        
        mid = head
        end = head
        while end.next is not None:
            end = end.next
            if end.next is not None:
                end = end.next
            mid = mid.next

        ptr = mid.next
        prev = mid
        while ptr is not None:
            nxt = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = nxt
        
        mid.next.next = None
        mid.next = None

        # Now start and end are 2 seperated linked lists pointing opp direction

        list1 = head
        list2 = end

        while list1 is not None and list2 is not None:
            nxt1 = list1.next
            nxt2 = list2.next

            list1.next = list2
            if nxt1 is not None:
                list2.next = nxt1

            list1 = nxt1
            list2 = nxt2

