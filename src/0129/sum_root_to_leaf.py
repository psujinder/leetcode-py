# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        total_sum = 0

        queue = [(root, root.val)]

        while queue:
            node, num = queue.pop()

            if not node.left and not node.right:
                total_sum += num

            if node.left:
                queue.append((node.left, num * 10 + node.left.val))

            if node.right:
                queue.append((node.right, num * 10 + node.right.val))

        return total_sum
