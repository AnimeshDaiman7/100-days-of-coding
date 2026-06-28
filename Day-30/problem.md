# Day 30 - Path Sum

## Problem

Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values equals targetSum.

### Example

Input:

root = [5,4,8,11,null,13,4,7,2,null,null,null,1]
targetSum = 22

Output:

true

## Approach

- Use DFS recursion.
- Subtract the current node value from targetSum.
- If a leaf node is reached, check whether the remaining sum equals the node value.
- Search both left and right subtrees.

## Complexity

- Time Complexity: O(n)
- Space Complexity: O(h)

## Platform

LeetCode #112 - Path Sum
