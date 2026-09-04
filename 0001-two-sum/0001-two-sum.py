class Solution(object):
    def twoSum(self, nums, target):
        num_map={}
        for i, num in enumerate(nums):
            complement=target-num
        
            if complement in num_map:
                return [i,num_map[complement]]
            
            num_map[num] = i
