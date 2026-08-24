class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pro = 0
        z = 0
        for n in nums:
            if n==0:
                z += 1
            else:
                if pro==0:
                    pro = 1
                pro *= n
        if z==1:
            for i in range(len(nums)):
                if nums[i]==0:
                    nums[i]=pro
                else: nums[i] = 0
            return nums
        elif z>1:
            return [0]*len(nums)
        
        for i in range(len(nums)):
            nums[i] = int(pro/nums[i])
        return nums