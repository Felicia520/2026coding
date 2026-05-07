# week11-4.py 學習計畫 Binary Search Tree 第2題
# LeetCode 450. Delete Node in a BST
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def findRightest(root):  # 找到最右邊那個人
            if root.right:  # 右邊還有1
                return findRightest(root.right)  # 繼續往右邊走
            return root  # 沒有右邊，那就 你 自己上

        if root==None: return root
        if root.val==key:
            if root.left:
                now =  findRightest(root.left)  # 找到繼承者 now
                root.val = now.val  # 把繼承者的 直 塞進來
                root.left = self.deleteNode(root.left, now.val)
            else:
                return root.right
            # root.val = 999  # 代表要殺
        root.left = self.deleteNode(root.left, key)
        root.right = self.deleteNode(root.right, key)
        return root
