"""
Each node needs exactly 1 coin. Let a subtree’s balance be totalCoins - totalNodes
In postorder DFS, gather left/right balances; moves needed are abs(left) + abs(right) (coins crossing the edges)
Return this node’s balance: root.val + left + right - 1
"""
"""
Time Complexity: O(n) (visit each node once)
Space Complexity: O(h) recursion stack (worst O(n), avg O(log n) for balanced tree)
"""

from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left:'Optional[TreeNode]'=None, right:'Optional[TreeNode]'=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(level: List[Optional[int]]) -> Optional[TreeNode]:

    if not level:
        return None
    it = iter(level)
    root_val = next(it)
    if root_val is None:
        return None
    root = TreeNode(root_val)
    q = deque([root])
    for a, b in zip(it, it): 
        node = q.popleft()
        if a is not None:
            node.left = TreeNode(a)
            q.append(node.left)
        if b is not None:
            node.right = TreeNode(b)
            q.append(node.right)
    return root


class coinDistribution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            L = dfs(node.left)
            R = dfs(node.right)
            self.moves += abs(L) + abs(R)
            return node.val + L + R - 1
        dfs(root)
        return self.moves

if __name__ == "__main__":
    s = coinDistribution()

    cases = [
        ([1], 0),                         
        ([3,0,0], 2),                     
        ([0,3,0], 3),                     
        ([1,0,0,None,3], 4),            
        ([0,0,0,0,0,0,7], 12),          
    ]

    for level, expected in cases:
        root = build_tree(level)
        ans = s.distributeCoins(root)
        print(ans)
