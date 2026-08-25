class Solution(object):
    def search(self, nums, tar):
        low,high = 0, len(nums)-1

        while low<=high:
            mid = (low + high)//2

            if nums[mid] == tar:
                return mid

            elif nums[mid] < nums[high]:
                if (nums[mid] < tar) and (tar <=nums[high]) :
                    low = mid + 1
                else:
                    high = mid-1
            else:
                if (nums[low] <= tar) and (tar < nums[mid]) :
                    high = mid - 1
                else:
                    low = mid + 1
        return -1

        """
        1,3
        i j
        m
        """