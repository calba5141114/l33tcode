class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x > 0 or x == 0:
            # if integer is positive reverse int
            reversed = int(str(x)[::-1])
            if reversed == x:
                return True 
            else:
                return False
        else:
            return False
        
'''
Runtime beats 89.67 % of python3 submissions.
memory usage beats 47.89 % of python3 submissions.
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
'''
        
       
