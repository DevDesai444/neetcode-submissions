class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(-1)
        temp = dummy

        temp1, temp2 = list1, list2

        while temp1 is not None and temp2 is not None:
            if temp1.val < temp2.val:
                temp.next = temp1
                temp1 = temp1.next
            else:
                temp.next = temp2
                temp2 = temp2.next
            temp = temp.next

        if temp1 is not None:
            temp.next = temp1
        else:
            temp.next = temp2

        return dummy.next