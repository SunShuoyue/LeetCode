# Definition for Two Pointers binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        l = self.levelOrder(root.left)
        r = self.levelOrder(root.right)
        if len(l) >= len(r):
            res = [l[i]+r[i] for i in range(len(r))] + l[len(r):]
        return res.insert([root.val])