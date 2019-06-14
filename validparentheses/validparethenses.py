class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = { '(': ')', '[': ']', '{': '}' }
        for c in s:
            if c in match:
                # checking for match in dict
                stack.append(c)
            else:
                if not stack or match[stack.pop()] != c:
                    return False
        # returns inverse
        return not stack
