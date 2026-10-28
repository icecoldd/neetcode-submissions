class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsSeen = set()
        for num in nums:
            if num in numsSeen:
                return True
            numsSeen.add(num)
        return False