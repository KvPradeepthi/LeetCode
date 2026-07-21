class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        nums.reverse()
        nums[:k]=nums[:k][::-1]
        nums[k:]=nums[k:][::-1]
        return nums