class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = dict()

        for i, num in enumerate(nums):
            if target-num in num_dict:
                return sorted([i, num_dict[target-num]])
            if num not in num_dict:
                num_dict[num] = i




