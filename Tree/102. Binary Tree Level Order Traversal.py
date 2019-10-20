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
        if not root:
            return []
        l = []
        r = []
        if root.left:
            l = self.levelOrder(root.left)
            if not l:
                l = []
        if root.right:
            r = self.levelOrder(root.right)
            if not r:
                r = []
        if len(l) >= len(r):
            res = [l[i] + r[i] for i in range(len(r))] + l[len(r):]
        else:
            res = [l[i] + r[i] for i in range(len(l))] + r[len(l):]
        res.insert(0, [root.val])
        return res
