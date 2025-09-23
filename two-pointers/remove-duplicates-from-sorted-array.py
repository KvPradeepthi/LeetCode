class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # If the array is empty, there are no unique elements
        if not nums:
            return 0
        
        # Initialize a pointer to keep track of the unique elements
        unique_ptr = 0
        
        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            # If the current element is different from the element at the unique pointer
            if nums[i] != nums[unique_ptr]:
                # Move the unique pointer forward and replace the element with the new unique element
                unique_ptr += 1
                nums[unique_ptr] = nums[i]
        
        # Return the number of unique elements (unique_ptr is zero-indexed, so we return unique_ptr + 1)
        return unique_ptr + 1
