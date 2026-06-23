# Day 25 - Merge Two Sorted Lists

## Problem

Given the heads of two sorted linked lists, merge them into one sorted linked list and return its head.

### Example

Input:

list1 = [1,2,4]
list2 = [1,3,4]

Output:

[1,1,2,3,4,4]

## Approach

- Create a dummy node.
- Compare nodes from both lists.
- Attach the smaller node to the merged list.
- Continue until one list is exhausted.
- Attach remaining nodes.

## Complexity

- Time Complexity: O(n + m)
- Space Complexity: O(1)

## Platform

LeetCode #21 - Merge Two Sorted Lists
