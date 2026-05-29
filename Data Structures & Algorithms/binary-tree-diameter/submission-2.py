# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    diameter = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root.right == None and root.left == None:
            return 0
        self.parseNodes(root)
        return self.diameter
    
    def parseNodes(self, root: Optional[TreeNode]):
        if root == None:
            return
        sum_diam = self.maxDepth(root.right) + self.maxDepth(root.left)
        if self.diameter < sum_diam:
            self.diameter = sum_diam
        self.parseNodes(root.right)
        self.parseNodes(root.left)
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        right_depth = 1 + self.maxDepth(root.right)
        left_depth = 1 + self.maxDepth(root.left)
        if right_depth > left_depth:
            return right_depth
        else:
            return left_depth    