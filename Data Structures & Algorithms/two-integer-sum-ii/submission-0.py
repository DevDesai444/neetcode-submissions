class Solution(object):
    def twoSum(self, nums, tar):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # hashm = {} # nums[i] -> [is]
        # for i in range(len(nums)) :
        #     if nums[i] not in hashm:
        #         hashm[nums[i]] = [i]
        #         continue
        #     hashm[nums[i]].append(i)
        
        # for i in range(len(nums)) :
        #     rem = tar - nums[i]
        #     if rem in hashm:
        #         # for j in hashm[rem]:
        #         #     if j>i:
        #         #         return [i+1,j+1]
        #         #     continue
        #         return [i+1,hashm[rem][-1]+1]
        #     continue
        """
        [2,7,11,15]
           i     j

        """
        l, r = 0, len(nums) - 1
        while l < r:
            total = nums[l] + nums[r]
            if total == tar:
                return [l + 1, r + 1]
            elif total < tar:
                l += 1
            else:
                r -= 1