'''
https://www.geeksforgeeks.org/problems/maximum-path-sum-from-any-node/1
'''

#########################################################################################
##########################  DFS Post-Order (Path Through Node)  Approach  ##########################

'''
PROBLEM STATEMENT:
------------------
Given a binary tree, find the maximum path sum where a path is any sequence
of nodes from any node to any node (not necessarily through the root).
A path must contain at least one node and cannot revisit nodes.
Goal: Return the maximum sum among all possible paths in the tree.

APPROACH - DFS POST-ORDER WITH GLOBAL MAX:
-------------------------------------------
Key Insight: For every node, the best path passing through it is:
  node.data + (best gain from left subtree) + (best gain from right subtree)
A subtree contributes 0 if its best path sum is negative (better to not include it).

Strategy:
- Use DFS post-order so left and right subtree results are available before processing a node
- At each node, clamp negative child contributions to 0 (ignore bad subtrees)
- Update a global maximum with the full path through the current node (left + node + right)
- Return only the best single-branch gain upward (node + max(left, right)) to the parent,
  because a path cannot fork at two levels simultaneously

ALGORITHM STEPS:
----------------
1. Initialize self.maxi = -infinity (handles all-negative trees)
2. DFS post-order on each node:
   a. Recurse left → left_sum; if left_sum < 0, set left_sum = 0
   b. Recurse right → right_sum; if right_sum < 0, set right_sum = 0
   c. Candidate path through this node = node.data + left_sum + right_sum
   d. Update self.maxi = max(self.maxi, candidate)
   e. Return node.data + max(left_sum, right_sum) to parent (single branch only)
3. Return self.maxi

EXAMPLE WALKTHROUGH:
--------------------
Input:
        -10
        /  \\
       9   20
          /  \\
         15   7

DFS on 9:   left=0, right=0 → candidate=9,  maxi=9,  return 9
DFS on 15:  left=0, right=0 → candidate=15, maxi=15, return 15
DFS on 7:   left=0, right=0 → candidate=7,  maxi=15, return 7
DFS on 20:  left=15, right=7 → candidate=20+15+7=42, maxi=42, return 20+15=35
DFS on -10: left=9, right=35 → candidate=-10+9+35=34, maxi=42, return -10+35=25

Answer: 42  (path: 15 → 20 → 7)

COMPLEXITY ANALYSIS:
--------------------
Time Complexity: O(n)
- Each node is visited exactly once in the DFS traversal

Space Complexity: O(h)
- h is the height of the tree (recursion call stack); O(log n) balanced, O(n) worst case
'''

#########################################################################################

''' Structure of binary tree node
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def findMaxSum(self, root): 
        # code here
        self.maxi = float('-inf')
        
        def solve(node):
            if node is None:
                return 0
                
                
            left_sum = solve(node.left)
            if left_sum < 0:
                left_sum = 0
            
            right_sum = solve(node.right)
            if right_sum < 0:
                right_sum = 0
            
            self.maxi = max(self.maxi, node.data + left_sum + right_sum)
            return node.data+max(left_sum, right_sum)
            
        solve(root)    
        return self.maxi
	
#########################################################################################