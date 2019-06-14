class Solution:
    def reverse(self, x: int) -> int:
        
        result = x
        if x > 0 or  x == 0  :
            # if positive case
            result = int(str(x)[::-1])
        else:
             # if negative case
             result = int(str(abs(x))[::-1]) * -1
            
        if(abs(result) > (2 ** 31 -1)):
            # if integer is not signed 32bit
            return 0
        else:
            return result
           
              
'''
 beats 99.36 % of python3 submissions.
 memory usage beats 44.32 % of python3 submissions.
'''
