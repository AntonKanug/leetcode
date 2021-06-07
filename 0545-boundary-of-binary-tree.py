# https://leetcode.com/problems/boundary-of-binary-tree/submissions/
# O(n) time, space

# Idea
# Get left boundary by going left
# Ger right boundary by going right
# Get the leaves in each dir

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    values = []
    values2 = []
    noDup1 = True
    noDup2 = True
    
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        self.values = []
        self.values2 = []
        self.noDup1 = True
        self.noDup2 = True

        self.values.append(root.val)
        
        if root.left:
            self.values.append(root.left.val)
            self.getLeft(root.left)
            self.getLeftLeaves(root.left)
        if root.right:
            self.values2.append(root.right.val)
            self.getRight(root.right)
            self.getRightLeaves(root.right)

        return self.values + self.values2[::-1]
    
    def getLeft(self,root):
        if root == None: return
        if root.left:
            self.values.append(root.left.val)
            self.getLeft(root.left)
        elif root.right:
            self.values.append(root.right.val)
            self.getLeft(root.right)

    def getRight(self,root):
        if root == None: return
        if root.right:
            self.values2.append(root.right.val)
            self.getRight(root.right)
        elif root.left:
            self.values2.append(root.left.val)
            self.getRight(root.left)
            

            
    def getLeftLeaves(self,root):
        if root == None: return
        if root.left == None and root.right == None:
            
            # Avoid duplicate leaf
            if self.values[-1] == root.val and self.noDup1:
                self.noDup1 = False
            else: self.values.append(root.val)

        self.getLeftLeaves(root.left)
        self.getLeftLeaves(root.right)
        
    def getRightLeaves(self,root):
        if root == None: return
        if root.left == None and root.right == None:
            
            # Avoid duplicate leaf
            if self.values2[-1] == root.val and self.noDup2:
                self.noDup2 = False
            else: self.values2.append(root.val)

        self.getRightLeaves(root.right)
        self.getRightLeaves(root.left)
        

