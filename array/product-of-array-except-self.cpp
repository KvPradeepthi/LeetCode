class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
         int n = nums.size(); // Get the size of the input array
        vector<int> answer(n, 1); // Create answer vector initialized with ones
        
        int leftProduct = 1; // Variable to store running product from the left
        for (int i = 0; i < n; i++) { // Loop from left to right
            answer[i] = leftProduct; // Assign running left product to answer
            leftProduct *= nums[i]; // Update running left product
        }
        
        int rightProduct = 1; // Variable to store running product from the right
        for (int i = n - 1; i >= 0; i--) { // Loop from right to left
            answer[i] *= rightProduct; // Multiply existing answer by running right product
            rightProduct *= nums[i]; // Update running right product
        }
        
        return answer; // Return final result vector
  
        
    }
};