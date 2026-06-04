# Day 6 - Invert Binary Tree

## Problem

Given the root of a binary tree, invert the tree and return its root.

### Example

Input:
root = [4,2,7,1,3,6,9]

Output:
[4,7,2,9,6,3,1]

## Approach

- Use recursion to visit each node.
- Swap the left and right child.
- Recursively invert the left and right subtrees.

## Complexity

- Time Complexity: O(n)
- Space Complexity: O(h)

## Platform

LeetCode #226 - Invert Binary Tree
