class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        size = len(nums)
        result = []

        i = 0
        while i < size - 2:
            j = i+1
            k = size - 1
            if i > 0 and nums[i] == nums[i-1]:
                i+=1
                continue
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    if j > i+1 and nums[j] == nums[j-1]:
                        j+=1
                        continue
                    result.append([nums[i], nums[j], nums[k]])
                    j+=1
                    k = size - 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j+=1
                else:
                    k-=1
            i+=1
        
        return result