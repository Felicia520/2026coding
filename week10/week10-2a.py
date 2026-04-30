# week10-2a.py 學習計畫 Binary Search Tree - DFS
# DFS 深度優先搜尋 tree 最喜歡用「涵是呼叫式」
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            if root == None: return 0
            left = helper(root.left)
            right = helper(root.right)
            return max(left, right) + 1
        return helper(root)
