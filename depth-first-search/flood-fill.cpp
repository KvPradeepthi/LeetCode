class Solution {
public:
     void dfs(vector<vector<int>>& image, int r, int c, int color, int originalColor) { // Depth-first search helper function
        int rows = image.size(); // Get total number of rows
        int cols = image[0].size(); // Get total number of columns
        
        if (r < 0 || c < 0 || r >= rows || c >= cols || image[r][c] != originalColor) { // Check boundaries and if pixel matches original color
            return; // Return if out of bounds or color does not match
        }
        
        image[r][c] = color; // Update current pixel to new color
        
        dfs(image, r + 1, c, color, originalColor); // Visit down neighbor
        dfs(image, r - 1, c, color, originalColor); // Visit up neighbor
        dfs(image, r, c + 1, color, originalColor); // Visit right neighbor
        dfs(image, r, c - 1, color, originalColor); // Visit left neighbor
    }

    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) { // Main flood fill function
        int originalColor = image[sr][sc]; // Store starting pixel color
        if (originalColor != color) { // Check if new color is different from original color to avoid infinite recursion
            dfs(image, sr, sc, color, originalColor); // Call depth-first search function
        }
        return image; // Return modified image
    }
};