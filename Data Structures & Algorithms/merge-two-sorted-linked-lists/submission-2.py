class Solution:
    def mergeTwoLists(self, list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val > list2.val:
            list1, list2 = list2, list1

        head = list1

        while (list1.next is not None) and (list2 is not None):
            if list1.next.val <= list2.val:
                list1 = list1.next
            else:
                t = list2.next
                list2.next = list1.next
                list1.next = list2
                list1 = list1.next
                list2 = t

        if (list2 is not None):
            list1.next = list2

        return head