# week09-6.py 學習計畫 Linked List 第2題
# LeetCode 328. Odd Even Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = []
        while head:
            a.append( head.val )
            head = head.next

        N = len(a)
        now = ans = ListNode()
        for i in range(0,N,2):
            now.next = ListNode( a[i])
            now = now.next
        for i in range(1, N, 2):
            now.next = ListNode( a[i] )
            now = now.next
        return ans.next
