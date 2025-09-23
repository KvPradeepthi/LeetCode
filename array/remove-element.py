class Solution(object):
    def removeElement(self, nums, val):
        k = 0  # Pointer to track the position of the next element to place
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]  # Move the element to the 'k' position
                k += 1  # Increment 'k' to the next position
        return k

        
        