# Day 18 - Diameter of Binary Tree

## Problem

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in the tree.

## Approach

- Use DFS to calculate subtree heights.
- For each node, compute:
  diameter = left_height + right_height
- Keep track of the maximum diameter encountered.

## Complexity

- Time Complexity: O(n)
- Space Complexity: O(h)

## Platform

LeetCode #543 - Diameter of Binary Tree
