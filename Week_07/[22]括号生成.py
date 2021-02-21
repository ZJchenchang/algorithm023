# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。 
# 
#  
# 
#  示例： 
# 
#  输入：n = 3
# 输出：[
#        "((()))",
#        "(()())",
#        "(())()",
#        "()(())",
#        "()()()"
#      ]
#  
#  Related Topics 字符串 回溯算法 
#  👍 1511 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        s = ''
        res = []
        def gener(s, left, right):
            while left == n and right == n:
                res.append(s)
                return
            if left < n:
                gener(s + '(', left + 1, right)
            if right < n and right < left:
                gener(s + ')', left, right + 1)
        gener(s, 0, 0)
        return res




# leetcode submit region end(Prohibit modification and deletion)
