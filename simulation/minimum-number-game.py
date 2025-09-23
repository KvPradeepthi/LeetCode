class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        arr = []
        
        # Process in pairs
        for i in range(0, len(nums), 2):
            alice = nums[i]       # smaller
            bob = nums[i+1]       # next smaller
            arr.append(bob)       # Bob appends first
            arr.append(alice)     # Alice appends second
        
        return arr

        