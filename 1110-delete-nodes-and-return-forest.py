# https://leetcode.com/problems/delete-nodes-and-return-forest/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        
        output = []
        
        def helper(root, to_del, new):
            if not root: return
            
            # Set parent property
            if root.left: root.left.parent = root
            if root.right: root.right.parent = root
                
            if new and root.val not in to_del: output.append(root)
                
            new = False
            
            # If value in set
            if root.val in to_del:
                new = True
                # Remove it from the parent
                if root.parent:
                    if root.parent.left == root:
                        root.parent.left = None
                    else: root.parent.right = None
                
            # Recurse
            helper(root.left, to_del, new)
            helper(root.right, to_del, new)
                
        root.parent = None
        helper(root, set(to_delete), True)
        
        return output