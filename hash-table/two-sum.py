class Solution(object):
    def twoSum(self, nums, target):
        mp={}
        for i,num in enumerate(nums):
            need=target-num
            if need in mp:
                return [mp[need],i]
            mp[num]=i



        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
       
        # Create a dictionary to hold the number and its index
        num_to_index = {}

        # Iterate over the list
        for index, num in enumerate(nums):
            # Calculate the complement
            complement = target - num

            # Check if complement is in the dictionary
            if complement in num_to_index:
                # If found, return the pair of indices
                return [num_to_index[complement], index]
            
            # If not found, add the current number and its index to the dictionary
            num_to_index[num] = index

        # If no pair is found (though the problem assures one exists), return an empty list
        return []


        