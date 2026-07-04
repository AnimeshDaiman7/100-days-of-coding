# Day 36 - Kth Largest Element in an Array

## Problem

Given an integer array `nums` and an integer `k`, return the kth largest element in the array.

Note:
It is the kth largest element in the sorted order, not the kth distinct element.

### Example

Input:
nums = [3,2,1,5,6,4]
k = 2

Output:
5

## Approach

- Maintain a Min Heap of size k.
- Insert every element into the heap.
- If heap size exceeds k, remove the smallest element.
- After processing all numbers, the heap's top element is the kth largest.

## Complexity

- Time Complexity: O(n log k)
- Space Complexity: O(k)

## Platform

LeetCode #215 - Kth Largest Element in an Array
