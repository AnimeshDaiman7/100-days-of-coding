# Day 8 - Min Stack

## Problem

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

- push(val)
- pop()
- top()
- getMin()

All operations should work in O(1) time.

## Approach

- Maintain two stacks:
  - Main stack to store all elements.
  - Min stack to keep track of the minimum element.
- Whenever a new minimum is encountered, push it onto the min stack.
- While popping, remove from the min stack if the popped element is the current minimum.

## Complexity

- Time Complexity: O(1) for all operations.
- Space Complexity: O(n)

## Platform

LeetCode #155 - Min Stack
