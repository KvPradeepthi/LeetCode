class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        sums=0
        for i in range(len(accounts)):
            l=0
            for j in range(len(accounts[0])):
                l=l+accounts[i][j]
            if l>sums:
                sums=l
        return sums

        