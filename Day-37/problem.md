# Day 37 - Validate Binary Search Tree

## Problem

Given the root of a binary tree, determine if it is a valid Binary Search Tree (BST).

A valid BST satisfies:

- Left subtree contains only nodes with values less than the current node.
- Right subtree contains only nodes with values greater than the current node.
- Both left and right subtrees must also be valid BSTs.

### Example

Input:
root = [2,1,3]

Output:
true

## Approach

- Traverse the tree recursively.
- Maintain lower and upper bounds for every node.
- If a node violates its allowed range, return False.
- Otherwise, recursively validate both subtrees with updated bounds.

## Complexity

- Time Complexity: O(n)
- Space Complexity: O(h)

## Platform

LeetCode #98 - Validate Binary Search Tree
