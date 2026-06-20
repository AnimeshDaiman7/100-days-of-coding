# Day 22 - Remove Nth Node From End of List

## Problem

Given the head of a linked list, remove the nth node from the end of the list and return its head.

### Example

Input:

head = [1,2,3,4,5]
n = 2

Output:

[1,2,3,5]

## Approach

- Create a dummy node.
- Use fast and slow pointers.
- Move fast pointer n+1 steps ahead.
- Move both pointers until fast reaches the end.
- Remove the target node.

## Complexity

- Time Complexity: O(n)
- Space Complexity: O(1)

## Platform

LeetCode #19 - Remove Nth Node From End of List
