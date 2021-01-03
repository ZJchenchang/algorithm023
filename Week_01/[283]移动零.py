# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。 
# 
#  示例: 
# 
#  输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0] 
# 
#  说明: 
# 
#  
#  必须在原数组上操作，不能拷贝额外的数组。 
#  尽量减少操作次数。 
#  
#  Related Topics 数组 双指针 
#  👍 901 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 第一种办法，从左往右遍历原数组，每当遇到不是零的数值，就和左边的0交换位置。
        # 其实可以理解为有两个数组。j是前面非零数组的最右下标，i是后边0数组的最左下标
        # j = 0
        # for i in range(len(nums)):
        #     if nums[i] != 0:
        #         nums[j], nums[i] = nums[i], nums[j]
        #         j += 1
        # # 语法问题：这里为啥不用return？

        # 第二种办法，1.还是先从左往右遍历数组，遇到不是零的数值就赋值给左边；
        # 2.同时用count记录遇到的非0的个数。
        # 3.最后把count + 1这个位置后面的数重新赋值为0
        count = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[count] = nums[i]
                count += 1
        for j in range(count, len(nums)):
            nums[j] = 0
# leetcode submit region end(Prohibit modification and deletion)
