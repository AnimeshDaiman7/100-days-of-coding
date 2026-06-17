# Day 19 - Binary Search

## Problem

Given a sorted array of integers and a target value, return its index if found. Otherwise, return -1.

The solution must run in O(log n) time.

## Approach

- Use Binary Search.
- Compare the target with the middle element.
- If target is larger, search the right half.
- If target is smaller, search the left half.
- Continue until the target is found or the search space becomes empty.

## Complexity

- Time Complexity: O(log n)
- Space Complexity: O(1)

## Platform

LeetCode #704 - Binary Search
