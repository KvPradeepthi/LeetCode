from typing import List
from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums_str = list(map(str, nums))
        def compare(x, y):
            return (int(y + x) - int(x + y))
        nums_str.sort(key=cmp_to_key(compare))
        result = ''.join(nums_str)
        return '0' if result[0] == '0' else result
