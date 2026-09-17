class Solution:
    def climbStairs(self, n: int) -> int:
        # if n==1 or n==0:
        #     return 1
        # return self.climbStairs(n-1) + self.climbStairs(n-2)

        # dp = [-1]*(n+1)
        # def helper(n):
        #     if n==1 or n==0:
        #         return 1
        #     if dp[n]!=-1:
        #         return dp[n]
        #     dp[n] = helper(n-1) + helper(n-2)
        #     return dp[n]
        # return helper(n)


        dp = [-1]*(n+1)

        for i in range(n+1):
            if i==1 or i==0:
                dp[i]=1
            else: dp[i] = dp[i-1] + dp[i-2]
        return dp[n]