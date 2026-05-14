# week12-5.py 學習計畫 Graphs - DFS 第四題
# LeetCode 399. Evaluate Division
# 有很多分子、分母 的除法關係
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        path = defaultdict(list)
        for(a, b), v in zip(equations,values):
            path[a].append( (b, v) )
            path[b].append( (a, 1/v) )
        def helper(now,target, v0):
            if now not in path or target not in path: return -1
            if now == target: return v0
            visited.add(now)
            ans = -1
            for node, v in path[now]:
                if node not in visited:
                    ans = max(ans, helper(node, target, v0*v))
            return ans
        ans = []
        for a, b in queries:
            visited = set()
            ans.append( helper(a, b, 1))
        return ans
