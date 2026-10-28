class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output_list = []
        seen_dict = {}
        i = 0

        for string in strs:
            sorted_word = "".join(sorted(string))
            if sorted_word not in seen_dict:
                output_list.append([string])
                seen_dict[sorted_word] = i
                i+=1
            else:
                output_list[seen_dict[sorted_word]].append(string)
        
        return output_list