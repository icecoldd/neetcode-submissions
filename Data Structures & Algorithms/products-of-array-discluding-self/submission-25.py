class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numsSize = len(nums)

        if numsSize == 2:
            return [nums[1], nums[0]]

        prefix = []
        suffix = [0] * numsSize
        result = []

        i, j = 0, numsSize - 1

        while(i < numsSize):
            if i == 0:
                prefix.append(nums[i])
                suffix[j] = nums[j]
            else:
                prefix.append(prefix[i-1] * nums[i])
                suffix[j] = suffix[j+1] * nums[j]
            i+=1
            j-=1

        for i in range(numsSize):
            if i == 0:
                result.append(suffix[1])
                continue
            if i == numsSize - 1:
                result.append(prefix[numsSize - 2])
                continue
            result.append(prefix[i-1] * suffix[i+1])

        return result