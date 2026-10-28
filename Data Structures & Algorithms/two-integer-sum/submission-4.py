class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # output does not need to be sorted in ascending order
        # the earliest occurence of a seen combo does not need to be returned
        # any two indexes that are not the same as each other is valid

        num_dict = dict()

        for i, num in enumerate(nums):
            if target-num in num_dict:
                return [num_dict[target-num], i]
            num_dict[num] = i




