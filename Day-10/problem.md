# Day 10 - Maximum Depth of Binary Tree

## Problem

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

### Example

Input:
root = [3,9,20,null,null,15,7]

Output:
3

## Approach

- Use recursion.
- Calculate the maximum depth of the left and right subtrees.
- Return 1 plus the larger depth.

## Complexity

- Time Complexity: O(n)
- Space Complexity: O(h)

## Platform

LeetCode #104 - Maximum Depth of Binary Tree
