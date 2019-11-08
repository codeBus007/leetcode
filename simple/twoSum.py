# coding: utf-8
from typing import List

"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 
class Solution:

    # 迭代遍历
    def  twoSum_1(self, nums: List[int], target:int) -> List[int]:
        length = len(nums)
        if length <= 1:
            return []

        for i in range(length-1):
            current = nums[i]
            for j in range(1, length):
                if nums[j] == target - current:
                    return [i, j]

            return []

    # 使用字典哈希
    def  twoSum_2(self, nums: List[int], target:int) -> List[int]:
        dic = {}
        for i, num in enumerate(nums):
            if target - num in dic:
                return [dic[target-num], i]
            dic[num] = i




if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    s = Solution()
    print(s.twoSum_1(nums, target))
    print(s.twoSum_2(nums, target))



    