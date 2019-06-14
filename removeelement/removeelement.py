class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        next_free = 0 
        for i, num in enumerate(nums):
            if num != val:
                nums[next_free] = num
                next_free += 1
        return next_free
    
'''
Runtime: 36 ms, faster than 86.62% of Python3 online submissions for Remove Element.
Memory Usage: 13.2 MB, less than 26.22% of Python3 online submissions for Remove Element.
Given an array nums and a value val, remove all instances of that value in-place and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.
'''
