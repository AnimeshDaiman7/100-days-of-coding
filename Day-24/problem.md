# Day 24 - Lowest Common Ancestor of a Binary Search Tree

## Problem

Given a Binary Search Tree (BST), find the Lowest Common Ancestor (LCA) of two given nodes.

### Example

Input:

root = [6,2,8,0,4,7,9,null,null,3,5]
p = 2
q = 8

Output:

6

## Approach

- Utilize the BST property.
- If both nodes are smaller than the current node, move left.
- If both nodes are greater than the current node, move right.
- Otherwise, the current node is the LCA.

## Complexity

- Time Complexity: O(h)
- Space Complexity: O(1)

## Platform

LeetCode #235 - Lowest Common Ancestor of a Binary Search Tree
