# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    # def reverseList3(self, head):
    #     temp = 

    def reverseList(self, head):
        if (head is None) or (head.next is None):
            return head
        temp1=head.next
        temp2=head

        rev_head = self.reverseList(head.next)
        rev_tail = head.next
        rev_tail.next = head
        head.next = None
        return rev_head