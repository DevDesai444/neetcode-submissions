class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i, j = 0, len(height)-1
        mv = 0
        while i<j:
            v = (j-i) * (min(height[i],height[j]))
            if mv<=v:
                mv = v
            if height[i]<height[j] :
                i+=1
            else : # if height[j]<height[i] :
                j-=1
        return mv