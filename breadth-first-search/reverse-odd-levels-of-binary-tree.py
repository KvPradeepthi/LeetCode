# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def reverseOddLevels(self, root):
        if not root:
            return None
        
        # Initialize the queue for level order traversal
        queue = deque([root])
        level = 0
        
        # Traverse the tree level by level
        while queue:
            level_size = len(queue)
            current_level = []
            
            # Collect nodes at the current level
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node)
                
                # Enqueue left and right children for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # If we are at an odd level, reverse the values
            if level % 2 == 1:
                # Reverse the current level's values
                for i in range(len(current_level) // 2):
                    current_level[i].val, current_level[-(i + 1)].val = current_level[-(i + 1)].val, current_level[i].val
            
            # Move to the next level
            level += 1
        
        return root
        

        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        