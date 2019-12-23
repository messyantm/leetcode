"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

"""
from typing import List

"""暴力解法"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for f_index, f_value in enumerate(nums):
            for s_index, s_value in enumerate(nums[f_index + 1:]):
                if f_value + s_value == target:
                    return [f_index, f_index + s_index + 1]


"""hash解法"""


class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        import collections
        hash_map = collections.defaultdict(list)
        for index, value in enumerate(nums):
            hash_map[value].append(index)
        for k, v in hash_map.items():
            target_index = hash_map.get(target - k, None)
            if target_index is not None:
                if k == target - k:
                    if len(v) >= 2:
                        return [v[0], v[1]]
                else:
                    return [v[0], target_index[0]]


"""
hash优化
1.不保存相同值的index，每次只最新值的index
2.遍历的同时，生成hash表
3.不会出现index相同的情况
"""


class Solution3:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = dict()
        for index, value in enumerate(nums):
            s_index = hash_map.get(target - value, None)
            if s_index is not None:
                return [index, s_index]
            hash_map[value] = index
