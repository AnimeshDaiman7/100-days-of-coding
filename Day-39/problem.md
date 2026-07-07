# Day 39 - Construct Binary Tree from Preorder and Inorder Traversal

## Problem

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

### Example

Input:

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

Output:

[3,9,20,null,null,15,7]

## Approach

- Store each value's index from inorder traversal in a hashmap.
- The first element of preorder is always the root.
- Split the inorder array into left and right subtrees.
- Recursively construct the left subtree first, followed by the right subtree.

## Complexity

- Time Complexity: O(n)
- Space Complexity: O(n)

## Platform

LeetCode #105 - Construct Binary Tree from Preorder and Inorder Traversal
