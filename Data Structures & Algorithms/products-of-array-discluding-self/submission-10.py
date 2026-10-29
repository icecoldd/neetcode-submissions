class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_counter = 0
        seen_zero_position = 0
        i = 0

        while i < len(nums):
            if nums[i] == 0:
                zero_counter += 1
                seen_zero_position = i
                if zero_counter >= 2:
                    return [0 for _ in range(len(nums))]
                i+=1
                continue
            product *= nums[i]
            i+=1

        if zero_counter == 1:
            result = [0 for _ in range(len(nums))] 
            result[seen_zero_position] = product
            return result
        
        result = []
        for num in nums:
            result.append(int(product/num))
        
        return result