class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        close_tokens = [")", "]", "}"]
        open_tokens = ["(", "[", "{"]
        close_open_map = {
            ")": "(", 
            "]": "[", 
            "}": "{"
        }
        stack = []
        for i in range(len(s)):
            if s[i] in open_tokens:
                stack.append(s[i])
            elif s[i] in close_tokens:
                if len(stack) == 0:
                    return False
                elif stack.pop() <> close_open_map.get(s[i], ""):
                    return False
        return len(stack) == 0
print Solution().isValid("()[]{}")
print Solution().isValid("([)]")               
