class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = filter(lambda x: x.isalnum(), s.lower())
        #return self.isPalindrome2(s)
        if len(s) <= 1:
            return True
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] <> s[r]:
                return False
            else:
                l += 1
                r -= 1
        return True



    def isPalindrome2(self, s):
        if len(s) <= 1:
            return True
        elif len(s) <= 3:
            return s[0] == s[-1]
        else:
            return s[0] == s[-1] and self.isPalindrome2(s[1:-1])

print Solution().isPalindrome("A man, a plan, a canal: Panama")
print Solution().isPalindrome("race a car")
        
