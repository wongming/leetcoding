#https://leetcode-cn.com/problems/evaluate-reverse-polish-notation/

"""
思路：
    
"""

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

if __name__ == '__main__':
    tokens = ["2", "1", "+", "3", "*"]
    val = 9
    print Solution().evalRPN(tokens) == '((2 + 1) * 3) = 9'   
 
    tokens = ["4", "13", "5", "/", "+"]
    val = 6
    out = '(4 + (13 / 5)) = 6'
    print Solution().evalRPN(tokens) == out 
 
    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", \
        "+"]
    val == 22
