# 给定一个 N 叉树，返回其节点值的前序遍历。 
# 
#  例如，给定一个 3叉树 : 
# 
#  
# 
#  
# 
#  
# 
#  返回其前序遍历: [1,3,5,6,2,4]。 
# 
#  
# 
#  说明: 递归法很简单，你可以使用迭代法完成此题吗? Related Topics 树 
#  👍 128 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

# Definition for a Node.
from typing import List
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        stack, res = [root], []  # 设置一个栈用来存放遍历的节点
        while stack:
            root = stack.pop()
            res.append(root.val)
            stack.extend(root.children[::-1])  # 把子节点全部倒序入栈。因为栈是先入后出
        return res

        
# leetcode submit region end(Prohibit modification and deletion)
