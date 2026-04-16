# week08-4.py 學習計畫 Binary Search 第2題
# LeetCode 2300. Successful Pairs of Spells and Potions
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort() # 藥水「小到大」排好
        P = len(potions) # 有P種藥水
        ans = []
        for spell in spells:
            now = P - bisect_left(potions, success/spell)
            ans.append(now)
        return ans
