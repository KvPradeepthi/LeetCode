class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Sort the array
        nums.sort()
        
        # Define the binary search bounds
        low = 0
        high = nums[-1] - nums[0]
        
        # Helper function to count the number of pairs with distance <= mid
        def countPairs(mid):
            count = 0
            j = 0
            # Two-pointer technique
            for i in range(len(nums)):
                while j < len(nums) and nums[j] - nums[i] <= mid:
                    j += 1
                count += j - i - 1
            return count
        
        # Binary search on the distance
        while low < high:
            mid = (low + high) // 2
            if countPairs(mid) >= k:
                high = mid
            else:
                low = mid + 1
        
        return low
