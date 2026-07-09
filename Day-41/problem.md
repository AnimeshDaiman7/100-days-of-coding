# Day 41 - Average of Levels in Binary Tree

## Problem

Given the root of a binary tree, return the average value of the nodes on each level in the form of an array.

Answers within 10⁻⁵ of the actual answer will be accepted.

### Example

Input:
root = [3,9,20,null,null,15,7]

Output:
[3.00000,14.50000,11.00000]

## Approach

- Traverse the tree level by level using a queue.
- For every level:
  - Calculate the sum of node values.
  - Count the number of nodes.
  - Compute the average.
- Append each average to the answer list.

## Complexity

- Time Complexity: O(n)
- Space Complexity: O(n)

## Platform

LeetCode #637 - Average of Levels in Binary Tree
