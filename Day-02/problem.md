# Day 2 - Remove Linked List Elements

## Problem

Given the head of a linked list and an integer val, remove all the nodes of the linked list that have Node.val == val, and return the new head.

### Example 1

Input:
head = [1,2,6,3,4,5,6]
val = 6

Output:
[1,2,3,4,5]

### Example 2

Input:
head = []
val = 1

Output:
[]

### Example 3

Input:
head = [7,7,7,7]
val = 7

Output:
[]

## Approach

- Create a dummy node before the head.
- Traverse the linked list.
- If the next node contains the target value, remove it.
- Otherwise move to the next node.
- Return the new head.

## Complexity

- Time Complexity: O(n)
- Space Complexity: O(1)

## Platform

LeetCode #203 - Remove Linked List Elements
