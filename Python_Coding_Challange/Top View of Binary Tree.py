'''
https://www.geeksforgeeks.org/problems/top-view-of-binary-tree/1
'''

#########################################################################################
##########################  BFS with Horizontal Distance (Level Order)  Approach  ##########################

'''
PROBLEM STATEMENT:
------------------
Given a binary tree, return the top view — the set of nodes visible when the tree
is viewed from the top (i.e., from directly above).
For each vertical column, only the first node encountered from the top is visible.
Goal: Return nodes in the top view from left to right.

APPROACH - BFS WITH HORIZONTAL DISTANCE (HD):
----------------------------------------------
Key Insight: Assign a horizontal distance (HD) to every node: root=0, left child=HD-1,
right child=HD+1. The top view is the first node seen at each unique HD during a
level-order (BFS) traversal — BFS guarantees we see higher nodes before lower ones.

Strategy:
- Use BFS so nodes are processed level by level (top to bottom)
- Track the horizontal distance of each node alongside it in the queue
- For each HD, record only the first node encountered (skip if HD already in result)
- Sort the result dict by HD to produce the left-to-right output order

ALGORITHM STEPS:
----------------
1. Initialize result={} (HD → node data), queue with (root, HD=0)
2. BFS loop while queue is not empty:
   a. Dequeue (node, line)
   b. If line not in result → result[line] = node.data  (first node at this HD)
   c. Enqueue left child with (line - 1) if it exists
   d. Enqueue right child with (line + 1) if it exists
3. Sort result by key (HD) and collect values into ans list
4. Return ans

EXAMPLE WALKTHROUGH:
--------------------
Input:
        1
       / \\
      2   3
       \\
        4
         \\
          5
           \\
            6

HD assignments: 1→0, 2→-1, 3→1, 4→0, 5→1, 6→2

BFS order and result dict updates:
  (1, 0)  → result={0:1}
  (2,-1)  → result={0:1, -1:2}
  (3, 1)  → result={0:1, -1:2, 1:3}
  (4, 0)  → HD 0 already exists, skip
  (5, 1)  → HD 1 already exists, skip
  (6, 2)  → result={0:1, -1:2, 1:3, 2:6}

Sorted by HD: [-1:2, 0:1, 1:3, 2:6]
Answer: [2, 1, 3, 6]

COMPLEXITY ANALYSIS:
--------------------
Time Complexity: O(n log n)
- BFS visits each node once: O(n); sorting the HD keys: O(n log n)

Space Complexity: O(n)
- Queue holds at most O(w) nodes (w = max tree width); result dict holds O(n) entries
'''

#########################################################################################

'''
class Node:
    def __init__(self, val):
        self.data( = val
        self.left = None
        self.right = None
'''

from collections import deque


class Solution:
    def topView(self, root):
        # code here
        ans = []
        result = {}
        queue = deque([])
        queue.append([root,0])
        
        while queue:
            e, line = queue.popleft()
            if line not in result:
                result[line] = e.data
            if e.left:
                queue.append([e.left,line - 1])
            if e.right:
                queue.append([e.right,line + 1])
            
        for value in sorted(result.items()):
            ans.append(value[1])
            
        return ans
	
#########################################################################################