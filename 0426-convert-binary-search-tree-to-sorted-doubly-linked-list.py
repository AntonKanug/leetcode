# https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/submissions/
# O(n) - Time
# O(n) - Space, output arr + recursion (lgn) 

# Idea (Inorder): 
# Traverse bst by going left first, append cur val
# Taverse right

# Connect output arr by doubly linking it

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root: return None
        
        output = []
        def dfs(x):
            if not x: return
            dfs(x.left)
            output.append(x)
            dfs(x.right)
            
        dfs(root)
        
        for i in range(len(output)):
            output[i].right = output[(i+1) % len(output)]
            output[i].left = output[i-1]

        return output[0]
        
