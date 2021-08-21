# https://leetcode.com/problems/design-an-expression-tree-with-evaluate-function/

import abc 
from abc import ABC, abstractmethod 
"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""

class Node(ABC):
    @abstractmethod
    # define your fields here
    def evaluate(self) -> int:
        pass


class ExpressionNode(Node):
    
    def __init__(self, operator, left = None, right = None):
        self.operator = operator
        self.left = left
        self.right = right
        
    def evaluate(self):
        if self.operator == '+':
            return self.left.evaluate() + self.right.evaluate()
        if self.operator == '-':
            return self.left.evaluate() - self.right.evaluate()
        if self.operator == '*':
            return int(self.left.evaluate() * self.right.evaluate())
        if self.operator == '/':
            return self.left.evaluate() // self.right.evaluate()
        
class ValueNode(Node):
    
    def __init__(self, val):
        self.val = val
    
    def evaluate(self):
        return self.val
        
"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""

class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        stack = []
        lastNode = None
        
        for i in postfix:
            if i in ['+', '-', '*', '/']:
                x = stack.pop()
                y = stack.pop()
                lastNode = ExpressionNode(i, y, x)
                stack.append(lastNode)
            else:
                stack.append(ValueNode(int(i)))
        return lastNode
		
"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""
        