# Day 88 - Reverse Nodes in k-Group

## Problem

Given the head of a linked list, reverse the nodes of the list `k` at a time
and return the modified list.

If the number of remaining nodes is less than `k`, those nodes should remain
as they are.

The values of the nodes cannot be changed. Only the nodes themselves may
be rearranged.

### Example

Input:

head = [1,2,3,4,5], k = 2

Output:

[2,1,4,3,5]

Another example:

Input:

head = [1,2,3,4,5], k = 3

Output:

[3,2,1,4,5]

## Approach

- Create a dummy node before the head.
- Find the kth node from the current group.
- If there are fewer than `k` nodes remaining, stop.
- Reverse the current group using pointer manipulation.
- Connect the reversed group with the previous and next parts of the list.
- Move to the next group and repeat.

Only the links between nodes are changed.

## Complexity

- Time Complexity: O(n)
- Space Complexity: O(1)

## Platform

LeetCode #25 - Reverse Nodes in k-Group
