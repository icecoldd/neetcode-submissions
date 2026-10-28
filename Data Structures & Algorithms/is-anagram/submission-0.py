class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s_chars = sorted(s)
        sorted_t_chars = sorted(t)

        return sorted_s_chars == sorted_t_chars