# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and uses only constant extra space.

# Method 1

def findDuplicate1(nums) -> int:
    seen_elements = set()
    
    for num in nums:
        if num in seen_elements:
            return num
        seen_elements.add(num)
        

# Method 2
def findDuplicate2(nums) -> int:
        slow = nums[nums[0]]
        fast = nums[nums[nums[0]]]
        
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
            
        fast = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            
        return slow
    


