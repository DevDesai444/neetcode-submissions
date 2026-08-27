# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None

        winS = winE = head

        for i in range(n):
            winE = winE.next
            if winE is None:
                return head.next

        while winE.next:
            winE = winE.next
            winS = winS.next
        winS.next = winS.next.next
        return head