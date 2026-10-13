'''
https://www.geeksforgeeks.org/problems/bottom-view-of-binary-tree/1
'''

#########################################################################################
##########################  BFS with Horizontal Distance (Level Order)  Approach  ##########################

'''
PROBLEM STATEMENT:
------------------
Given a binary tree, return the bottom view — the set of nodes visible when the tree
is viewed from directly below.
For each vertical column, only the last node encountered from the top is visible.
Goal: Return nodes in the bottom view from left to right.

APPROACH - BFS WITH HORIZONTAL DISTANCE (HD):
----------------------------------------------
Key Insight: Assign a horizontal distance (HD) to every node: root=0, left child=HD-1,
right child=HD+1. The bottom view is the LAST node seen at each unique HD during a
level-order (BFS) traversal — BFS guarantees we process lower nodes after higher ones,
so each overwrite of result[HD] ends up keeping the deepest node.

Strategy:
- Use BFS so nodes are processed level by level (top to bottom)
- Track the horizontal distance of each node alongside it in the queue
- For each HD, always overwrite result[HD] with the current node (last one wins)
- Sort the result dict by HD to produce the left-to-right output order

Note: This is almost identical to Top View — the only difference is that Top View
skips an HD if already seen, while Bottom View always overwrites it.

ALGORITHM STEPS:
----------------
1. Initialize result={} (HD → node data), queue with (root, HD=0)
2. BFS loop while queue is not empty:
   a. Dequeue (node, line)
   b. result[line] = node.data  (always overwrite — last/deepest node at this HD wins)
   c. Enqueue left child with (line - 1) if it exists
   d. Enqueue right child with (line + 1) if it exists
3. Sort result by key (HD) and collect values into ans list
4. Return ans

EXAMPLE WALKTHROUGH:
--------------------
Input:
        20
       /  \\
      8    22
     / \\     \\
    5  3     25
      / \\
     10  14

HD assignments: 20→0, 8→-1, 22→1, 5→-2, 3→0, 25→2, 10→-1, 14→1

BFS order and result dict updates:
  (20, 0)  → result={0:20}
  (8, -1)  → result={0:20, -1:8}
  (22, 1)  → result={0:20, -1:8, 1:22}
  (5, -2)  → result={0:20, -1:8, 1:22, -2:5}
  (3, 0)   → result={0:3,  -1:8, 1:22, -2:5}   ← overwrites 20
  (25, 2)  → result={0:3,  -1:8, 1:22, -2:5, 2:25}
  (10,-1)  → result={0:3,  -1:10,1:22, -2:5, 2:25}  ← overwrites 8
  (14, 1)  → result={0:3,  -1:10,1:14, -2:5, 2:25}  ← overwrites 22

Sorted by HD: [-2:5, -1:10, 0:3, 1:14, 2:25]
Answer: [5, 10, 3, 14, 25]

COMPLEXITY ANALYSIS:
--------------------
Time Complexity: O(n log n)
- BFS visits each node once: O(n); sorting the HD keys: O(n log n)

Space Complexity: O(n)
- Queue holds at most O(w) nodes (w = max tree width); result dict holds O(n) entries
'''

#########################################################################################

'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

from collections import deque


class Solution:
    def bottomView(self, root):
        # code here
        ans = []
        result = {}
        queue = deque([])
        queue.append([root,0])
        while queue:
            e, line = queue.popleft()
            result[line] = e.data
            if e.left:
                queue.append([e.left,line - 1])
            if e.right:
                queue.append([e.right,line + 1])
                
        for value in sorted(result.items()):
            ans.append(value[1]) 
            
        return ans
	
#########################################################################################