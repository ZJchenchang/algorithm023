# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。 
# 
#  你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。 
# 
#  你可以按任意顺序返回答案。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [2,7,11,15], target = 9
# 输出：[0,1]
# 解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [3,2,4], target = 6
# 输出：[1,2]
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [3,3], target = 6
# 输出：[0,1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= nums.length <= 103 
#  -109 <= nums[i] <= 109 
#  -109 <= target <= 109 
#  只会存在一个有效答案 
#  
#  Related Topics 数组 哈希表 
#  👍 9952 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)-1):   # 暴力枚举法是每个小白应掌握的方法，因为不受语言本身带有的函数限制。
        #     for j in range(i+1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return

        # hashtabal = {} # 这个Python字典类型（哈希表）的本质：sums列表的值作为此哈希表的key，然后把原sums列表的索引当做这个哈希表的数值
        # for i, sumvalue in enumerate(nums):
        #     answer = target - sumvalue
        #     if answer in hashtabal:
        #         return[hashtabal[answer], i]
        #     hashtabal[sumvalue] = i
        # return []

        # hashtable = dict()
        # for i, num in enumerate(nums):
        #     if target - num not in hashtable: # 和上面方法一样，只是判断逻辑相反
        #         hashtable[nums[i]] = i
        #         continue               # 特别注意，因为没有这个continue，程序会直接顺序执行下面的return语句，Pycharm报错“KeyError”
        #     return [hashtable[target - num], i]
        # return []

        # 网友写的广度优先，空间复杂度最优
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nums[i + 1:]:
                return i, nums[i + 1:].index(diff) + i + 1
# leetcode submit region end(Prohibit modification and deletion)
