# week13-5.py 學習計畫 Heap / Priority Queue 第3題
# LeetCode 2542. Maximum Subsequence Score
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # 先把 nums1 跟 nums2 合併起來
        # ex.[1,3,3,2]
        #    [2,1,3,4]
        N = len(nums1) # 陣列的長度
        a = [ (nums2[i], nums1[i]) for i in range(N)]  # 左右合併起來
        #print(a)
        #e.sort()  # 試試看:小到大排好
        #print(a)
        a.sort(reverse=True)  # 大到小排好

        heap = [a[i][1] for i in range(k)]
        heapify(heap)
        ans = total = sum(heap)
        ans = total * a[k-1][0]

        for i in range(k, len(nums2)):
            n2, n1 = a[i]
            heappush(heap, n1)
            total += n1 - heappop(heap)
            ans = max(ans, total*n2)
            return ans
