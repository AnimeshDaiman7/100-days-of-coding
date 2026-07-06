# Day 38 - Middle of the Linked List

## Problem

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

### Example

Input:
head = [1,2,3,4,5]

Output:
[3,4,5]

## Approach

- Initialize two pointers: slow and fast.
- Move slow one step at a time.
- Move fast two steps at a time.
- When fast reaches the end, slow points to the middle node.
- Return slow.

## Complexity

- Time Complexity: O(n)
- Space Complexity: O(1)

## Platform

LeetCode #876 - Middle of the Linked List
