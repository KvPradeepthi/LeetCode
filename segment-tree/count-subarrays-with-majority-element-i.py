class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        answer = 0
        for start in range(n):
            count = 0
            for end in range(start, n):
                if nums[end] == target:
                    count += 1
                length = end - start + 1
                if count > length // 2:
                    answer += 1
        return answer
        