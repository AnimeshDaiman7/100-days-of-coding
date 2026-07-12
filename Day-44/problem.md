# Day 44 - Binary Tree Right Side View

## Problem

Given the root of a binary tree, imagine yourself standing on the right side of it.

Return the values of the nodes you can see ordered from top to bottom.

### Example

Input:
root = [1,2,3,null,5,null,4]

Output:
[1,3,4]

## Approach

- Use Breadth-First Search (Level Order Traversal).
- Traverse each level using a queue.
- Store the last node visited at every level.
- Return the collected nodes.

## Complexity

- Time Complexity: O(n)
- Space Complexity: O(n)

## Platform

LeetCode #199 - Binary Tree Right Side View
