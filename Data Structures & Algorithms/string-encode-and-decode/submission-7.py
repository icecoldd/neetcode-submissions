class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_result = ""
        for string in strs:
            str_len = len(string)
            encoded_result += str(str_len) + "#" + string
        return encoded_result



    def decode(self, s: str) -> List[str]:
        stack = []
        result = []

        i = 0
        while i < len(s):
            if s[i] == '#' and stack:
                word_size = int("".join(stack))
                word = s[i+1 : i+word_size+1]
                result.append(word)
                i += word_size + 1
                stack = []
                continue
            stack.append(s[i])
            i+=1

        return result