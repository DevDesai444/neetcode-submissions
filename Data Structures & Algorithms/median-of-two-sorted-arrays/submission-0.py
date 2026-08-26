class Solution(object):
    def findMedianSortedArrays(self, a, b):
        c = a + b
        c.sort()
        len_c = len(c)

        if len_c % 2 == 0:
            return (c[len_c // 2] + c[len_c // 2 - 1]) / 2.0
        else:
            return c[len_c // 2]