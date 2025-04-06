from typing import List
from collections import deque, defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return []

        col_mapping = defaultdict(list)
        queue = deque([(root, 0)])
        min_col = 0
        max_col = 0

        while queue:

            node, col = queue.popleft()

            col_mapping[col].append(node.val)
            min_col = min(min_col, col)
            max_col = max(max_col, col)

            if node.left:
                queue.append((node.left, col - 1))

            if node.right:
                queue.append((node.right, col + 1))

        return [col_mapping[i] for i in range(min_col, max_col + 1)]
