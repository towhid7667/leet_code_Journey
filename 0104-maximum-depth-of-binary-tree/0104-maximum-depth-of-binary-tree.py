# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        # q = deque([root])
        # count = 0
        # while q:
        #     for i in range(len(q)):
        #         curr = q.popleft()
        #         if curr.right:
        #             q.append(curr.right)
        #         if curr.left:
        #             q.append(curr.left)
                
        #     count += 1
        # return count            
        stack = [[root, 1]]
        res = 0
        while stack:
            node, depth = stack.pop()
            if node:
                res = max(res , depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res