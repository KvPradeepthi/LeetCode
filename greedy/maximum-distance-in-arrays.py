class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        # Initialize the global minimum and maximum with the first array
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        max_distance = 0
        
        # Iterate through the rest of the arrays
        for i in range(1, len(arrays)):
            # Calculate distances using the current array's elements
            current_min = arrays[i][0]
            current_max = arrays[i][-1]
            
            # Calculate potential maximum distances
            max_distance = max(max_distance, abs(max_val - current_min), abs(current_max - min_val))
            
            # Update the global minimum and maximum
            min_val = min(min_val, current_min)
            max_val = max(max_val, current_max)
        
        return max_distance
      