# https://leetcode.com/problems/closest-leaf-in-a-binary-tree/submissions/

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findClosestLeaf(self, root: Optional[TreeNode], k: int) -> int:
        
        path = self.findPath(root, k, [])
        
        minVal = 0
        minDist = float('inf')
        dist = len(path)
        
        for i, d in enumerate(path):
            if d == 'L':
                val, tempDist = self.searchForLeaf(root.right)
                root = root.left
            if d == 'R':
                val, tempDist = self.searchForLeaf(root.left)
                root = root.right
                
            tempDist += dist + 1 
            
            if tempDist < minDist: 
                minVal = val
                minDist = tempDist
            dist -= 1   
        
        val, tempDist = self.searchForLeaf(root)

        if tempDist < minDist: 
            minVal = val
            mindDist = tempDist
        
        return minVal
        
        
    def findPath(self, root, tgt, path):
        if not root: return []
        if root.val == tgt: return path
            
        return self.findPath(root.left, tgt, path + ['L']) or self.findPath(root.right, tgt, path + ['R']) 
    
    
    def searchForLeaf(self, root):
        if not root: return (None,float('inf'))
        
        q = deque()
        
        q.append([root, 0])
        
        while q:
            root, dist = q.popleft()

            if not root.left and not root.right:
                return (root.val, dist)
            if root.left:
                q.append([root.left, dist+1])
            if root.right:
                q.append([root.right, dist+1])
                