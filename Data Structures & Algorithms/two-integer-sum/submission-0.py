class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ## check current value, mathematically calculate the required sum number via dictionary look up, if it does not exist continue to next index
        num_dict = dict()

        for i, num in enumerate(nums):
            if target-num in num_dict:
                return sorted([i, num_dict[target-num]])
            if num not in num_dict:
                num_dict[num] = i




