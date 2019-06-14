class Solution(object):

    def twoSum(self, nums, target):

        num_to_index = {}

        for (i, num) in enumerate(nums):
            if target - num in num_to_index:
                return [i, num_to_index[target - num]]
            num_to_index[num] = i

        return []
    
'''
At the time of submission this code was faster than 85.92% of all Python submissions 
and used 46.23% less memory than other Python solutions.
'''
