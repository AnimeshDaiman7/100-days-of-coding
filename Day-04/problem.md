# Day 4 - Same Tree

## Problem

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

## Approach

- Compare both nodes recursively.
- If both are null, return true.
- If one is null or values differ, return false.
- Recursively compare left and right subtrees.

## Complexity

- Time Complexity: O(n)
- Space Complexity: O(h)

## Platform

LeetCode #100 - Same Tree
