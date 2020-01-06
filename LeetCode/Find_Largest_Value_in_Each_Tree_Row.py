#https://leetcode.com/problems/find-largest-value-in-each-tree-row/submissions/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        c = 0
        res = []
        level = []
        ele = []
        if root == None:
            return res
        ele.append(root)
        level.append(ele)
        res.append(root.val)
        # print(len(level),c)
        while c != len(level):
            ele = []
            lm = []
            for i in range(0,len(level[c])):
                # print(level[c][i].val)
                if level[c][i].left:
                    ele.append(level[c][i].left)
                    lm.append(level[c][i].left.val)
                if level[c][i].right:
                    ele.append(level[c][i].right)
                    lm.append(level[c][i].right.val)
            if len(ele):
                level.append(ele)
                res.append(max(lm))
            c += 1
            # print(len(level),c)
        return res
