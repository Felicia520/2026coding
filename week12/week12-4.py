# week12-4.py 學習計畫 Graphs - DFS 第4題
# LeetCode 1466. Reorder Routes to Make All Paths Lead to the City Zero
# 有N個城市，有N-1條路，希望大家都走到 0 都是正向，但不是正向的，有幾條路?
# 解法: 從 0 出發，全部走過，路不對，就ans += 1
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        visited = set()
        path = defaultdict(list)
        for a, b in connections:
            path[a].append( (b, +1) )
            path[b].append( (a, -1) )

        def helper(now):
            ans = 0
            visited.add(now)
            for k, d in path[now]:
                if k not in visited:
                    if d== +1: ans += 1
                    ans += helper(k)
            return ans
        return helper(0)
