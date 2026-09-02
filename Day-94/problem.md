# Day 94 - Recover Binary Search Tree

## Problem

You are given the root of a Binary Search Tree (BST), where the values of
exactly two nodes of the tree were swapped by mistake.

Recover the tree without changing its structure.

### Example

Input:

root = [1,3,null,null,2]

Output:

[3,1,null,null,2]

Explanation:

The values `1` and `3` were swapped.

After swapping them back, the tree becomes a valid BST.

## Approach

- Perform an inorder traversal of the BST.
- A valid BST produces values in ascending order during inorder traversal.
- Keep track of the previously visited node.
- If the previous node's value is greater than the current node's value,
  an incorrect ordering is found.
- Store the first incorrect node and the current node.
- After traversal, swap the values of the two incorrect nodes.
- The structure of the tree remains unchanged.

## Complexity

- Time Complexity: O(n)
- Space Complexity: O(n) due to recursion stack.

## Platform

LeetCode #99 - Recover Binary Search Tree
