class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # adding two lists together
        nums1 +=  nums2
        # re-sorting
        nums1.sort()
        
        if len(nums1) % 2 == 0:   
            # even
            return (nums1[(len(nums1))//2] + nums1[(len(nums1))//2-1]) / 2
        else:
            # odd
           return nums1[(len(nums1)-1)//2]
'''
At the time of submission this code was faster than 90.71% of all Python submissions 
and used 84.37% less memory than other Python solutions.
'''
