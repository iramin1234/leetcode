class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numbers = {}
        for i, value in enumerate(nums):
            if numbers.get(value):
                return True
            else:
                numbers[value] = 1
        return False
