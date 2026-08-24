class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = set()
        for i in range(len(nums)):
            j, k = i+1, len(nums)-1
            # nums[i] + nums[j] + nums[k] == 0
            while j<k:
                csum = nums[i] + nums[j] + nums[k]
                if csum > 0 :
                    k-=1
                elif csum < 0 :
                    j+=1
                else: # csum == 0
                    ans.add((nums[i], nums[j], nums[k]))
                    while j < k and nums[j]==nums[j+1]:
                        j+=1
                    j+=1
                    while j < k and nums[k]==nums[k-1]:
                        k-=1
                    k-=1
        ansl = []
        for a in ans:
            ansl.append(list(a))
        return ansl