# week12-1a.py 學習計畫 Graphs - DFS 第1題
# LeetCode 841. Keys and Rooms
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        stack = [0]  # 我們利用 stack 裡面有待處理的房間, 一開始 房間0 是開的
        visited = set()  # 有去過、處理過的房間， 不要再進去了
        visited.add(0)  # 已經排好、代處理，下次有拿到要使，不要再放入 stack 囉
        while stack:  # 只要 stack  還有東西，就繼續處理
            now = stack.pop() # 吐出1個房間，現在要來處理
            for k in rooms[now]: # 把 room now 房間哩，所有的要使 k ，都拿來檢查
                if k in visited: continue  # 要使k對應的房間k看過了，別再檢查
                # 如果走到這裡，代表沒走過、沒有待處理的房間K
                stack.append(k)  # 加入stack 資料結構
                visited.add(k)  # 標記這個房間也代處理、其他不要再排處理
        return len(rooms) == len(visited) # 房間的數目，全部都參觀過了，成功
