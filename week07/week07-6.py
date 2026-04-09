# week07-6.py 學習計畫 Queue 第2題
# LeetCode 649. Dota2 Senate
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        print(senate, type(senate)) # 先印出senate
        print(list(senate), type(list(senate))) # 印出 list(senate)
        # 樓上兩行，印出 字串 list(...) 下面印出 deque(...)
        queue = deque(list(senate))
        banR, banD = 0, 0
        R, D = senate.count('R'), senate.count('D')
        while queue: # 進行「互相Ban」的遊戲
            now = queue.popleft() # 左邊兔出個字母，他要相滅「敵對陣營」
            if now=='R':
                if banR>0:
                    banR -= 1 # 用掉1個消滅的名額
                    R -= 1 # 馬上少掉一個人
                else:
                    banD += 1
                    queue.append(now)
            else:
                if banD > 0:
                    banD -= 1
                    D -= 1
                else:
                    banR += 1
                    queue.append(now)

            if R==0: return'Dire' #把 R 消滅光'D'就得勝
            if D==0: return'Radiant' #把 D 消滅光'R'就得勝
