class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int left = 0; // Initialize left pointer to start of array
        int right = nums.size() - 1; // Initialize right pointer to end of array
        
        while (left < right) { // Loop until pointers meet
            int mid = left + (right - left) / 2; // Find middle index safely to prevent overflow
            
            if (nums[mid] < nums[mid + 1]) { // Check if element is smaller than right neighbor
                left = mid + 1; // Move left pointer to right half
            } else {
                right = mid; // Move right pointer to left half including mid
            }
        }
        
        return left; // Return the peak index where left and right meet
    }
};