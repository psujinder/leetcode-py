from typing import List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_count = len(queue)

            for i in range(level_count):
                node = queue.popleft()

                if i == level_count -1:
                    result.append(node.val)
                
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return result
