class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        rem_map = {0: 1}   # remainder frequency
        psum = 0
        count = 0
        
        for num in nums:
            psum += num
            rem = psum % k
            
            if rem in rem_map:
                count += rem_map[rem]
            
            rem_map[rem] = rem_map.get(rem, 0) + 1
        
        return count