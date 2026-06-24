# Day 26 - Kth Smallest Element in a BST

## Problem

Given the root of a Binary Search Tree and an integer k, return the kth smallest value in the BST.

### Example

Input:

root = [3,1,4,null,2]
k = 1

Output:

1

## Approach

- Use inorder traversal.
- BST inorder traversal produces values in sorted order.
- Count visited nodes.
- Return the kth visited node.

## Complexity

- Time Complexity: O(H + k)
- Space Complexity: O(H)

## Platform

LeetCode #230 - Kth Smallest Element in a BST
