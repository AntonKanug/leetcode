# https://leetcode.com/problems/binary-tree-vertical-order-traversal/submissions/

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        q = deque()
        cols = {}
        minCol = float('inf')
        
        # val, col
        q.append([root, 0])
        
        while q:
            root, col = q.popleft()
            
            if col in cols: cols[col].append(root.val)
            else: cols[col] = [root.val]
            
            minCol = min(minCol, col)
            
            if root.left:
                q.append([root.left, col-1])
            if root.right:
                q.append([root.right, col+1])
                
        output = []    
        while minCol in cols:
            output.append(cols[minCol])
            minCol+=1
            
        return output
        