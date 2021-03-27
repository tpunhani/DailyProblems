# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def diameterOfBinaryTree(root: TreeNode) -> int:
    diameter = 0
    print(diameter)
        
    def longest_path(node):
        if not node:
            return 0
        nonlocal diameter
            
        left = longest_path(node.left)
        right = longest_path(node.right)
            
        diameter = max(diameter, left+right)
            
        return max(left, right) + 1
        
    longest_path(root)
    return diameter


