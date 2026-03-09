class Solution:
    def removeSubstring(self, s, k):
        merostalin = s
        pattern = '(' * k + ')' * k
        while pattern in merostalin:
            merostalin = merostalin.replace(pattern, '')
        return merostalin
