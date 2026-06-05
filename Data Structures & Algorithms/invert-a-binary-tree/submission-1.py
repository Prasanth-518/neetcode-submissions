# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None :
            return root
        r_node = root.right
        l_node = root.left
        root.right = self.invertTree(l_node)
        root.left = self.invertTree(r_node)
        return root
