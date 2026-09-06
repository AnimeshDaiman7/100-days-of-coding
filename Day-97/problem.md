# Day 97 - Find Minimum in Rotated Sorted Array II

## Problem

Given a sorted rotated array that may contain duplicates, return the
minimum element of the array.

## Example

Input:

nums = [2,2,2,0,1]

Output:

0

## Approach

- Use Binary Search.
- Compare the middle element with the rightmost element.
- If `nums[mid] > nums[right]`, search in the right half.
- If `nums[mid] < nums[right]`, search in the left half including `mid`.
- If both are equal, duplicates prevent us from knowing which side
  contains the minimum, so decrease `right` by one.
- Continue until `left == right`.

## Complexity

- Time Complexity: O(log n) average, O(n) worst case
- Space Complexity: O(1)

## Platform

LeetCode #154 - Find Minimum in Rotated Sorted Array II
