

#Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':

        seen = set()

        while p:
            seen.add(p)
            p = p.parent

        while q:
            if q in seen:
                return q
            q = q.parent

    
    def lowestCommonAncestor2(self, p: 'Node', q: 'Node') -> 'Node':

        p1, p2 = p,q

        while p1 != p2:
            
            p1 = p1.parent
            if not p1:
                p1 = q

            p2 = p2.parent
            if not p2:
                p1 = q
        
        return p1
        
    