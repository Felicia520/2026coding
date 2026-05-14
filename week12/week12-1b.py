# week12-1b.py 學習計畫 Graphs - DFS 第1題
# LeetCode 841. Keys and Rooms
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()  # 有去過、處理過的房間， 不要再進去了
        def helper(now):
            for k in rooms[now]:
                if k not in visited:
                    visited.add(k)
                    helper(k)
        visited.add(0)
        helper(0)
        return len(rooms) == len(visited)
