# Day 20 - Linked List Cycle

## Problem

Given the head of a linked list, determine if the linked list has a cycle.

## Approach

- Use Floyd's Cycle Detection Algorithm.
- Maintain two pointers:
  - Slow pointer moves one step.
  - Fast pointer moves two steps.
- If they ever meet, a cycle exists.
- If fast reaches the end, there is no cycle.

## Complexity

- Time Complexity: O(n)
- Space Complexity: O(1)

## Platform

LeetCode #141 - Linked List Cycle
