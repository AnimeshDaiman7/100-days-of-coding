# Day 47 - Flatten Binary Tree to Linked List

## Problem

Given the `root` of a binary tree, flatten the tree into a linked list.

The linked list should use the same `TreeNode` class where:

- The right child points to the next node.
- The left child is always `null`.

The linked list should follow the same order as a preorder traversal of the binary tree.

### Example

Input:
root = [1,2,5,3,4,null,6]

Output:
[1,null,2,null,3,null,4,null,5,null,6]

## Approach

- Traverse the tree starting from the root.
- If the current node has a left child:
  - Find the rightmost node of the left subtree.
  - Attach the current node's right subtree to it.
  - Move the left subtree to the right.
  - Set the left child to null.
- Continue until every node is processed.

This modifies the tree in-place while preserving preorder traversal.

## Complexity

- Time Complexity: O(n)
- Space Complexity: O(1)

## Platform

LeetCode #114 - Flatten Binary Tree to Linked List
