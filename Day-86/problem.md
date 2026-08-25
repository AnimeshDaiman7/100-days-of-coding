# Day 86 - Next Permutation

## Problem

Given an array of integers `nums`, find the next permutation of `nums`.

The next permutation is the next lexicographically greater arrangement
of the array.

If no greater permutation exists, rearrange the array into the lowest
possible order.

The modification must be done in-place using constant extra memory.

### Example

Input:

nums = [1,2,3]

Output:

[1,3,2]

Another example:

Input:

nums = [3,2,1]

Output:

[1,2,3]

## Approach

- Start from the right and find the first index `i` such that
  `nums[i] < nums[i + 1]`.
- This index is the pivot.
- If a pivot exists, find the first element from the right that is
  greater than `nums[i]`.
- Swap the pivot with that element.
- Reverse the portion of the array after the pivot.
- If no pivot exists, reverse the entire array.

This produces the smallest permutation that is greater than the current
permutation.

## Complexity

- Time Complexity: O(n)
- Space Complexity: O(1)

## Platform

LeetCode #31 - Next Permutation
