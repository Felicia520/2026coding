# week12-3.py 學習計畫 Graphs - DFS 第2題
# LeetCode 547. Number of Provinces
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)
        visited = set()

        def helper(now):
            visited.add(now)
            for k in range(N):
                if k not in visited and isConnected[now][k]:
                    helper(k)
        ans = 0
        for i in range(N):
            if i not in visited:
                ans += 1
                helper(i)
        return ans

