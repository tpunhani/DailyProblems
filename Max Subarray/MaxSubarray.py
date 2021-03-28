# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
def maxSubArray(nums) -> int:

# initialize with first element
    current_subarray = max_subarray = nums[0]
        
# run loop from 1st element and save maximum sum
    for i in nums[1:]:
        current_subarray = max(i, current_subarray+i)
        max_subarray = max(current_subarray, max_subarray)
            
    return max_subarray


