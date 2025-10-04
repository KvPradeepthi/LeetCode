from collections import deque

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        q = deque([(root, 1)])  # (node, depth)
        
        while q:
            node, depth = q.popleft()
            # If it's a leaf, return depth immediately
            if not node.left and not node.right:
                return depth
            if node.left:
                q.append((node.left, depth + 1))
            if node.right:
                q.append((node.right, depth + 1))
