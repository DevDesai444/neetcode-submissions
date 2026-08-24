class Solution:
    def trap(self, height: List[int]) -> int:
        i,j = 0, len(height)-1
        v = 0
        lm, rm = 0, 0
        while i<j :
            if height[i] < height[j]:
                if lm > height[i]:
                    v += lm - height[i]
                else:
                    lm = height[i]
                i+=1
            else: # height[i] >= height[j]:
                if rm > height[j]:
                    v += rm - height[j]
                else:
                    rm = height[j]
                j-=1
        return v
            # else: # height[i] == height[j]





        # for i in range(1, len(height)-1):
        #     if lm > height[i] < rm:
        #         v += min(lm, rm) - height[i]
        #     else:
        #         continue
        # return v