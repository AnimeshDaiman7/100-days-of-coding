# Day 35 - Implement Queue using Stacks

## Problem

Implement a First In First Out (FIFO) queue using only two stacks.

Implement the following operations:

- push(x)
- pop()
- peek()
- empty()

### Example

Input:
["MyQueue","push","push","peek","pop","empty"]

[[],[1],[2],[],[],[]]

Output:
[null,null,null,1,1,false]

## Approach

- Maintain two stacks:
  - inputStack for inserting elements.
  - outputStack for removing elements.
- Push directly into inputStack.
- Before pop/peek:
  - If outputStack is empty, transfer all elements from inputStack.
- Return values from outputStack.

## Complexity

- Push: O(1)
- Pop: Amortized O(1)
- Peek: Amortized O(1)
- Empty: O(1)

## Platform

LeetCode #232 - Implement Queue using Stacks
