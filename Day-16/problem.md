# Day 16 - Balanced Binary Tree

## Problem

Given a binary tree, determine if it is height-balanced.

A height-balanced binary tree is one in which the left and right subtrees of every node differ in height by no more than 1.

## Approach

- Use Depth First Search (DFS).
- Calculate the height of left and right subtrees recursively.
- If the difference exceeds 1 at any node, mark the tree as unbalanced.
- Return whether the tree is balanced.

## Complexity

- Time Complexity: O(n)
- Space Complexity: O(h)

## Platform

LeetCode #110 - Balanced Binary Tree
