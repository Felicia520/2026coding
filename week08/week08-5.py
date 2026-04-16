# wwek08-5.py 學習計畫 Binary Search 第3題
# LeetCode 62. Find Peak Element
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # 笨方法: for迴圈不行
        N = len(nums)
        for i in range(N):
            if i==0: #沒有左邊只有右邊
                if nums[i] > nums[i+1]: return i
            elif i ==N-1: # 最右邊、沒有右邊，指測左邊(要比左邊大)
                if nums[i] > nums[i-1]: return i
            # 下面會當機，因為 i-1 或 i+1 可能會超過範圍
            elif nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i
