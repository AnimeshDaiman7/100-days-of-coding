# Day 59 - Serialize and Deserialize Binary Tree

## Problem

Design an algorithm to serialize and deserialize a binary tree.

Serialization is the process of converting a binary tree into a string so it can be stored or transmitted.

Deserialization reconstructs the original binary tree from the serialized string.

There is no restriction on how the serialization/deserialization algorithm should work, as long as the original tree can be perfectly reconstructed.

### Example

Input:

root = [1,2,3,null,null,4,5]

Output:

[1,2,3,null,null,4,5]

## Approach

- Perform a preorder DFS traversal.
- Store node values in a list.
- Use `"N"` to represent null nodes.
- Join the list into a comma-separated string.
- During deserialization:
  - Read values sequentially.
  - Rebuild the tree recursively.
  - `"N"` represents a null node.

## Complexity

- Time Complexity: O(n)
- Space Complexity: O(n)

## Platform

LeetCode #297 - Serialize and Deserialize Binary Tree
