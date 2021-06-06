# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

def longestConsecutive(nums) -> int:
    unique_list = set(nums)
    longest_streak = 0
    for num in unique_list:
        if (num-1) not in unique_list:
            current_streak = 1
            while (num+1) in unique_list:
                current_streak += 1
                num += 1
                
        longest_streak = max(longest_streak, current_streak)
        
    return longest_streak





