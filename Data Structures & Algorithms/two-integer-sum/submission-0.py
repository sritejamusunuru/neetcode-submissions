class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for i, num in enumerate(nums):
            difference = target - num
            if difference in hash_table:
                return [hash_table[difference], i]
            else:
                hash_table[num] = i
