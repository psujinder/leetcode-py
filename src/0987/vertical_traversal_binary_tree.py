from typing import List
from collections import defaultdict, deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        nodes = []

        queue = deque([(0, 0, root)])

        while queue:
            col, row, node = queue.popleft()

            if node:
                nodes.append((col, row, node.val))

                if node.left:
                    queue.append((col - 1, row + 1, node.left))

                if node.right:
                    queue.append((col + 1, row + 1, node.right))
        
        nodes.sort()

        col_map = defaultdict(list)
        for col, row, val in nodes:
            col_map[col].append(val)

        return [col_map[x] for x in sorted(col_map)]
        

