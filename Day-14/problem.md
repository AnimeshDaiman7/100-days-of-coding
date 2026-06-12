# Day 14 - Symmetric Tree

## Problem

Given the root of a binary tree, check whether it is a mirror of itself.

### Example

Input:
root = [1,2,2,3,4,4,3]

Output:
true

## Approach

- Compare the left and right subtrees recursively.
- Check:
  - Node values are equal.
  - Left subtree mirrors right subtree.
  - Right subtree mirrors left subtree.

## Complexity

- Time Complexity: O(n)
- Space Complexity: O(h)

## Platform

LeetCode #101 - Symmetric Tree
