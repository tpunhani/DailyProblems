# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

def permute(nums: list[int]) -> list[list[int]]:
        res = []
        dfs(nums, [], res)
        return res
    
    
def dfs(dec_space, fixed_path, res):
    if not dec_space:
        res.append(fixed_path)
            
    for i in range(len(dec_space)):
        dfs(dec_space[:i] + dec_space[i+1:], fixed_path + [dec_space[i]], res)



