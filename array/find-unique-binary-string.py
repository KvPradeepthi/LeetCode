class Solution:
    def findDifferentBinaryString(self, nums):
        res = ""
        for i in range(len(nums)):
            if nums[i][i] == '0':
                res += '1'
            else:
                res += '0'
                
        return res