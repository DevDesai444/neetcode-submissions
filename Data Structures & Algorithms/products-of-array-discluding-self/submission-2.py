class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        ans = [1] * n

        pre = 1
        for i in range(n):
            ans[i] = pre
            pre *= nums[i]

        suf = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= suf
            suf *= nums[i]
            
        return ans