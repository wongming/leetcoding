operation_tokens = ["+", "-", "*", "/"]

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        oper_s = []
        char_s = []
        exp = []
        for ele in tokens:
            if ele in operation_tokens:
                s1 = char_s.pop()
                s2 = char_s.pop()
                if ele == "+":
                    val = s2 + s1
                elif ele == "-":
                    val = s2 - s1
                elif ele == "*":
                    val = s2 * s1
                elif ele == "/":
                    if s1 * s2 > 0:
                        val = s2 / s1
                    else:
                        val = (-1 * s2) / s1 * (-1)

                char_s.append(val)
            else:
                ele = int(ele)
                char_s.append(ele)
        return char_s.pop()
print Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
print Solution().evalRPN(["4","13","5","/","+"])
