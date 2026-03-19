# week04-3.py More Challenges 的簡單版
# Leetcode 3866. First Unique Even Element
# 找到陣列nums李「只出現過1次的偶數」第1次出現的位置
class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        N = len(nums) # 有N個數
        H =  [0] * 200 # 很多很多格，H[??] 對應 ?? 出現幾次
        for i in range(N): # 第一次處理
            H[ nums[i] ] += 1 # 把出現的數字，塞進H[??] 裡
        for i in range(N):
            if nums[i] % 2 == 0 and H[ nums[i] ] == 1: # 偶數, 只出現一次
                 return nums[i] #找到答案
        return -1
