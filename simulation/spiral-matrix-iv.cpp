/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> spiralMatrix(int m, int n, ListNode* head) {
         vector<vector<int>> matrix(m, vector<int>(n, -1)); // Create m x n matrix initialized with -1
        
        int top = 0; // Initialize top boundary
        int bottom = m - 1; // Initialize bottom boundary
        int left = 0; // Initialize left boundary
        int right = n - 1; // Initialize right boundary
        
        ListNode* curr = head; // Pointer to traverse the linked list
        
        while (top <= bottom && left <= right && curr != nullptr) { // Loop while boundaries are valid and nodes exist
            for (int j = left; j <= right && curr != nullptr; j++) { // Traverse from left to right on top row
                matrix[top][j] = curr->val; // Assign current node value to matrix cell
                curr = curr->next; // Move to next node in linked list
            }
            top++; // Shrink top boundary downwards
            
            for (int i = top; i <= bottom && curr != nullptr; i++) { // Traverse from top to bottom on right column
                matrix[i][right] = curr->val; // Assign current node value to matrix cell
                curr = curr->next; // Move to next node in linked list
            }
            right--; // Shrink right boundary inwards
            
            for (int j = right; j >= left && curr != nullptr && top <= bottom; j--) { // Traverse from right to left on bottom row
                matrix[bottom][j] = curr->val; // Assign current node value to matrix cell
                curr = curr->next; // Move to next node in linked list
            }
            bottom--; // Shrink bottom boundary upwards
            
            for (int i = bottom; i >= top && curr != nullptr && left <= right; i--) { // Traverse from bottom to top on left column
                matrix[i][left] = curr->val; // Assign current node value to matrix cell
                curr = curr->next; // Move to next node in linked list
            }
            left++; // Shrink left boundary inwards
        }
        return matrix; // Return the filled matrix
    }
};