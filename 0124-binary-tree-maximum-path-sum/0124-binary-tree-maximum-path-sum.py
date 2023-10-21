# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        found = [root.val]
        def dfs(root):
            if not root:
                return 0
            leftMax = dfs(root.left)    
            rightMax = dfs(root.right)
            leftMax  = max(leftMax, 0)    
            rightMax  = max(rightMax, 0)
            found[0] = max(found[0], leftMax + rightMax + root.val)
            return root.val + max(leftMax, rightMax)
        dfs(root)
        return found[0]        