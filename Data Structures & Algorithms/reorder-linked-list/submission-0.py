# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while (fast is not None) and (fast.next is not None):
            slow = slow.next
            fast = fast.next.next

        secP = slow.next
        slow.next = None

        temp1=secP
        temp2=None
        while(temp1 is not None):
            temp1_next = temp1.next
            temp1.next = temp2
            temp2 = temp1
            temp1 = temp1_next

        fstP = head
        while temp2 is not None:
            temp = fstP.next
            fstP.next = temp2
            temp2_next = temp2.next
            temp2.next = temp
            fstP = temp
            temp2 = temp2_next