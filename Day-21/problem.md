# 33. Search in Rotated Sorted Array

## Difficulty
Medium

## Problem Statement

There is an integer array `nums` sorted in ascending order with distinct values.

Before being passed to your function, `nums` may be rotated at an unknown pivot index.

Given the rotated array `nums` and an integer `target`, return the index of `target` if it exists in the array; otherwise, return `-1`.

You must write an algorithm with `O(log n)` runtime complexity.

---

## Example 1

Input:
nums = [4,5,6,7,0,1,2]
target = 0

Output:
4

---

## Example 2

Input:
nums = [4,5,6,7,0,1,2]
target = 3

Output:
-1

---

## Example 3

Input:
nums = [1]
target = 0

Output:
-1

---

## Approach

Use a modified Binary Search.

At every step:
1. Find the middle element.
2. Determine which half is sorted.
3. Check if the target belongs to that sorted half.
4. Discard the other half.
5. Continue until the target is found.

Since one half is always sorted, Binary Search can still be applied efficiently.

---

## Complexity Analysis

- Time Complexity: O(log n)
- Space Complexity: O(1)

---

## Concepts Used

- Binary Search
- Rotated Sorted Array
- Divide and Conquer
- Search Space Reduction

---

## Key Takeaway

Even though the array appears unsorted due to rotation, one side always remains sorted. Identifying the sorted portion allows us to maintain logarithmic search efficiency.
