# Day 64 - Binary Tree Maximum Path Sum

## Problem

Given the `root` of a binary tree, return the maximum path sum of any non-empty path.

A path is a sequence of nodes where each adjacent pair is connected by an edge. The path does not need to pass through the root.

### Example

Input:

root = [1,2,3]

Output:

6

Explanation:

The maximum path is 2 → 1 → 3, whose sum is 6.

## Approach

- Perform a post-order DFS.
- Compute the maximum gain from the left and right subtrees.
- Ignore negative gains.
- Update the global maximum using:
  - left gain + node value + right gain
- Return the larger branch gain to the parent.

## Complexity

- Time Complexity: O(n)
- Space Complexity: O(h)

Where:
- n = number of nodes
- h = height of the tree

## Platform

LeetCode #124 - Binary Tree Maximum Path Sum
