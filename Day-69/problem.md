# Day 69 - Merge k Sorted Lists

## Problem

You are given an array of `k` sorted linked lists.

Merge all the linked lists into one sorted linked list and return it.

### Example

Input:

lists = [[1,4,5],[1,3,4],[2,6]]

Output:

[1,1,2,3,4,4,5,6]

## Approach

- If there are no lists, return `None`.
- Repeatedly merge pairs of linked lists.
- Use the standard merge procedure for two sorted linked lists.
- Continue until only one merged list remains.

This Divide and Conquer approach reduces the number of merge operations.

## Complexity

- Time Complexity: **O(N log k)**
- Space Complexity: **O(1)** (excluding recursion stack)

Where:

- N = Total number of nodes
- k = Number of linked lists

## Platform

LeetCode #23 - Merge k Sorted Lists
