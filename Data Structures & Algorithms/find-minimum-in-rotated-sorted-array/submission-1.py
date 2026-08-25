class Solution(object):
    def findMin(self, nums):
        low, high, ans = 0, len(nums)-1, 5001

        while low<=high :
            mid = (low + high)//2

            if nums[mid] < nums[high]:
                ans = min(ans, nums[mid])
                high = mid - 1
            else :
                ans = min(ans, nums[low])
                low = mid + 1
        return ans