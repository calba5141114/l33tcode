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
        
       
