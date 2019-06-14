class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        next_new = 0 
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                nums[next_new] = nums[i]
                next_new += 1
        return next_new
    
    
    '''
    Runtime: 64 ms, faster than 56.42% of Python3 online submissions for Remove Duplicates from Sorted Array.
    Memory Usage: 15 MB, less than 13.99% of Python3 online submissions for Remove Duplicates from Sorted Array.
    Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
    Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
    '''
        
        
