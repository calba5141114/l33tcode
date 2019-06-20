class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        sum = int("".join([ str(x) for x in A])) + K
        sum = [ int(x) for x in str(sum)]
        return sum 
        
'''
Runtime: 228 ms, faster than 43.23% of Python3 online submissions for Add to Array-Form of Integer.
Memory Usage: 14 MB, less than 20.63% of Python3 online submissions for Add to Array-Form of Integer.
'''
