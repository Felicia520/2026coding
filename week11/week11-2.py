# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# week11-2.py 學習計畫 Binary Tree - DFS 最後一題
# LeetCode 236. Lowest Common Ancestor of a Binary Tree
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        a =[]
        def helper(root):
            count = 0  # 請問你下面累積幾個 p 或 q 的 node
            if root == None: return 0  #  沒有東西
            if root==p or root==q: count += 1  # 找到1個
            count += helper(root.left)
            count += helper(root.right)
            if count==2:  # 收集齊2個, 太好啦!
                a.append(root)  # 藥劑下答案
            return count  # 現在收集到第幾個? return count
        helper(root)  # 要記得 發動 寒士呼叫韓式
        return a[0]  # 最前面，第一次出現的答案
