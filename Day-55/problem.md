# Day 55 - Add Two Numbers

## Problem

You are given two non-empty linked lists representing two non-negative integers.

The digits are stored in reverse order, and each node contains a single digit.

Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

### Example

Input:

l1 = [2,4,3]
l2 = [5,6,4]

Output:

[7,0,8]

Explanation:

342 + 465 = 807

## Approach

- Create a dummy node to simplify linked list construction.
- Traverse both linked lists simultaneously.
- Add corresponding digits and carry.
- Store the current digit in a new node.
- Update the carry.
- Continue until both lists and carry are processed.
- Return the linked list starting after the dummy node.

## Complexity

- Time Complexity: O(max(n, m))
- Space Complexity: O(max(n, m))

## Platform

LeetCode #2 - Add Two Numbers
