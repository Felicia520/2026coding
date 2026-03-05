#week02-4.py
#LeetCode 11. Container With Most Water
class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0 # 一開始沒有答案
        i,j = 0, len(height) - 1
        while i < j: #只要左右還沒撞再一起
            area = (j-i) * min(height[i], height[j])
            ans = max(ans, area)
            if height[i] < height[j]: i += 1 #小的i，往右
            else: j-= 1 #小的j，往左
        return ans
