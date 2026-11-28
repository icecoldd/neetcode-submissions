class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False

        bracketPairs = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        stack = []
        for char in s:
            if char in bracketPairs:
                stack.append(char)
            else:
                if not stack:
                    return False
                if bracketPairs[stack.pop()] != char:
                    return False
        
        return not stack