# week11-5.py 學習計畫 Binary Tree - BFS 第1題
# LeetCode 199. Binary Tree Right Side View
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def helper(root, level):  # 第幾層樓
            if root==None: return
            if len(ans) <= level:
                ans.append(root.val)
            else:
                ans[level] = root.val
            helper(root.left, level+1)  # 函式呼叫函式
            helper( root.right, level+1)  # 函式呼叫函式

        helper(root,0)
        return ans
