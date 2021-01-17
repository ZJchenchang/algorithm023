# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。 
# 
#  示例: 
# 
#  输入: n = 4, k = 2
# 输出:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ] 
#  Related Topics 回溯算法 
#  👍 467 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def dfs(comlist, k, index, cur, res):
            if k == 0:
                res.append(cur)
                return
            for i in range(index, len(comlist) - k + 1):
                dfs(comlist, k - 1, i + 1, cur + [comlist[i]], res)
        dfs(range(1, n + 1), k, 0, [], res)
        return res
# leetcode submit region end(Prohibit modification and deletion)
