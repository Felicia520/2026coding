# week05-2a.py 學習計畫 Hash Map / Set
# LeetCode 2215. Find the Difference of Two Arrays
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans1 = [] #放「在nums1 但不在 nums2」的數
        for num in nums1: # 逐一取出
            if num not in nums2: #沒在裡面
                ans1.append(num) # 放入答案
        ans2 = []
        for num in nums2:
            if num not in nums1:
                ans2.append(num)
        return [list(set(ans1)), list(set(ans2))]
