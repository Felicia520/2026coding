# week15-4a.py 學習計畫 DP - Multidimensional 第4題
# LeetCode 72. Edit Distance 編輯幾次後會得到word2
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        M,N = len(word1), len(word2)
        @cache
        def helper(i,j):
            if i==M and j==N: return 0
            if i==M: return N-j
            if j==N: return M-i
            if word1[i]==word2[j]: return helper(i+1,j+1)
            #ans1 = helper(i+1,j)
            #ans2 = helper(i,j+1)
            #ans3 = helper(i+1,j+1)
            return min(helper(i+1,j), helper(i,j+1), helper(i+1,j+1)) + 1
        return helper(0,0)
