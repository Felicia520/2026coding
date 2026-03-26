# week05-5.py 厩策璸礶 Hash Map / Set
# LeetCode 1657. Determine if Two Strings Are Close
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        counter1 = Counter(word1) # 参璸ノ筁ダ瞷Ω计
        counter2 = Counter(word2)

        if set(counter1.keys()) != set(counter2.keys()): # ノダぃ碞ア毖
            return False
        # р瞷Ω计逼狦ㄢ娩常妓ê碞传妓ゎ
        if sorted(counter1.values()) != sorted(counter2.values()):
            return False
        return True
