import math
class Solution(object):
    def minEatingSpeed(self, piles, h):
        def banas(k):
            tot = 0
            for p in piles:
                tot += (p + k - 1) // k
            return tot

        ans = max(piles)
        low, high = 1, ans

        while low <= high:
            mid = (low+high)//2
            if banas(mid) <= h:
                ans = mid
                high = mid - 1
            else : # if banas(mid) > h:
                low = mid + 1
        return ans