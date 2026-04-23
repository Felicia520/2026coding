# week09-3.py 學習計畫 Linked List 第3題 Easy 版本(使用「函式呼叫函式」Recursion)
# week09-2.py 學習計畫 Linked List 第3題 Easy 版本
# LeetCode 206. Reverse Linked List
# 把它反過來
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:return head  # 終止條件

        head2 = head.next
        ans = self.reverseList(head.next)
        head2.next, head.next = head, None
        return ans
