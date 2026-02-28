class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        map={0:1}
        n=len(nums)
        c=0
        csum=0
        for i in range(n):
            csum+=nums[i]
            if csum - k in map:
                c += map[csum - k]
            
            map[csum] = map.get(csum, 0) + 1
        return c

        