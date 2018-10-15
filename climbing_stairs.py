class Solution(object):
    def climbStairs(self, n):
        l = [1, 2]
        for i in range(2, n):
            l[i].append(l[i-1] + l[i-2])
        return l[n]


    """
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n-2) + self.climbStairs(n-1)
    """
print Solution().climbStairs(2)
print Solution().climbStairs(3)
print Solution().climbStairs(35)
