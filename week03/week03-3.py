# week03-3.py 學習計畫 Sliding Window 第2題
# LeetCode 1456. Maximum Number of Vowels in a Substring of Given Length
# Substring of Given Length
# 母音 Vowels: a,e,u,o,。長度k的小字母,最多己祖母音
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou') #把5個字母,變成set()
        # 以後用 if c in vowels:就可以快速確認他是母音
        #以前 if c=='a' or c=='e' or c=='i' or c=='o' orc=='u'
        count = 0 # 紀錄目前有幾個母音
        for i in range(k): # 找前面k個母音, 逐一檢查, 看是不是答案
            if s[i] in vowels: count += 1 # 找到1個母音,開心!!!
        ans = count # 離開迴圈時, 確認前面的k個字母, 有count 個字母,先當答案
        N = len(s) # 全部字串的長度為N
        for i in range(k,N): #右邊的每一個字母, 逐一檢查
            if s[i] in vowels: count +=1 # 右邊的頭s[i] 又吃到1個母音,開心
            if s[i-k] in vowels: count -= 1 # 左邊尾巴 s[i-1]吐掉,失去1個
            ans = max(ans,count) # 更新答案, 找最大值
        return ans
