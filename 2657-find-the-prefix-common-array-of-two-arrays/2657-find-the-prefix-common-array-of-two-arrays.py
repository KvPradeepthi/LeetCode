from typing import List
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        seenA = set()
        seenB = set()
        ans = []
        common = 0
        for i in range(len(A)):
            seenA.add(A[i])
            seenB.add(B[i])
            if A[i] in seenB:
                common += 1
            if B[i] != A[i] and B[i] in seenA:
                common += 1
            ans.append(common)
        return ans