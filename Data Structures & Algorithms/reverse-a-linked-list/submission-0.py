# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        cur = head
        nxt = head.next
        cur.next=None

        while nxt:
            temp = nxt.next
            nxt.next = cur
            cur = nxt
            nxt = temp

        return cur