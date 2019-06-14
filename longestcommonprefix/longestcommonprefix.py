class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not strs:
            return ''
            
        strs.sort()
        first = strs[0]
        last = strs[-1]
        
        i = 0
        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1
        return first[:i]
        
'''
Runtime: 28 ms, faster than 99.56% of Python3 online submissions for Longest Common Prefix.
Memory Usage: 13.2 MB, less than 47.53% of Python3 online submissions for Longest Common Prefix.
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
'''
