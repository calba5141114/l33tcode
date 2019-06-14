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
    
    '''
    Runtime: 36 ms, faster than 86.22% of Python3 online submissions for Valid Parentheses.
    Memory Usage: 13.3 MB, less than 18.20% of Python3 online submissions for Valid Parentheses.
    Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
    An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Note that an empty string is also considered valid.
    '''
