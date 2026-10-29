class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_occurrences = {}
        sorted_frequency = [[None] for _ in range(len(nums))]
        
        for num in nums:
            if num not in num_occurrences:
                num_occurrences[num] = 1
            else:
                num_occurrences[num] += 1
        
        for key, value in num_occurrences.items():
            sorted_frequency[value-1].append(key)
        
        result_size = 0
        result = []
        for row in reversed(sorted_frequency):
            for item in reversed(row):
                if result_size == k:
                    break
                if item is not None:
                    result.append(item)
                    result_size += 1
        
        return result
                

            
