class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        from collections import Counter
        count = Counter(nums)
        return [num for num, freq in count.items() if freq == 2]
