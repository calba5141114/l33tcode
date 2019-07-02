# brute force
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # to keep track of the longest string
        longest = ''
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i:j][::-1] and j - i > len(longest):
                    longest = s[i:j]
        return longest
