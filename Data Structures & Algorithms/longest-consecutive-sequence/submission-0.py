class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        [100,4,200,101,2,,1,5,3,2,102,99] -> set
          i

        """
        numsset = set(nums)
        mcount = 0
        for n in numsset:
            if (n - 1) in numsset:
                continue
            count = 0
            while (n + count + 1) in numsset:
                count += 1
            if (count + 1) > mcount:
                mcount = count + 1
        return mcount