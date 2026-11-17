class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        longest_consecutive = 0
        for num in nums_set:
            if num-1 not in nums_set:
                count = 1
                i = num+1
                while(i in nums_set):
                    count+=1
                    i+=1
                
                if count > longest_consecutive:
                    longest_consecutive = count
                    
        return longest_consecutive


