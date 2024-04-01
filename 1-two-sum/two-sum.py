class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 2:
            return False
        dictionary = {}
        for i, num in enumerate(nums):
            difference = target - num
            if difference in dictionary:
                return [dictionary[difference], i]
            dictionary[num] = i
        return False
