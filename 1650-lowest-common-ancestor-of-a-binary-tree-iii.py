# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/

"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        pp, qq = p, q
        
        while pp != qq:
            pp = pp.parent if pp.parent else q
            qq = qq.parent if qq.parent else p
        
        return pp
        
#         ip, iq = 0, 0
#         ppath, qpath = self.getPath(p,[]), self.getPath(q,[])

#         while ip < len(ppath) and iq < len(qpath) and ppath[ip] == qpath[iq]:
#             ip+=1
#             iq+=1

#         return ppath[ip-1]
        
        
    def getPath(self,root,path):
        if not root: return path
        return self.getPath(root.parent, [root] + path)