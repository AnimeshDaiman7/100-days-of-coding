# Day 71 - Count of Smaller Numbers After Self

## Problem

Given an integer array `nums`, return an integer array `counts` where `counts[i]` is the number of smaller elements to the right of `nums[i]`.

### Example

Input:

nums = [5,2,6,1]

Output:

[2,1,1,0]

## Approach

- Use a modified Merge Sort.
- Store each element together with its original index.
- During the merge process, compare elements from the left and right halves.
- Whenever an element from the right half is smaller than an element from the left half, increase the count of smaller elements for that left element.
- Place the elements back in sorted order.

This allows us to count smaller elements while performing the merge.

## Complexity

- Time Complexity: O(n log n)
- Space Complexity: O(n)

## Platform

LeetCode #315 - Count of Smaller Numbers After Self
