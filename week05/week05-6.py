# week05-6.py ¾Ç²ß­pµe Hash Map / Set
# LeetCode 2352. Equal Row and Column Pairs
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
       counter = Counter()
       for row in grid:
            counter[ tuple(row) ] += 1
       ans = 0
       for col in zip(*grid):
            ans += counter[ tuple(col)]
       return ans
