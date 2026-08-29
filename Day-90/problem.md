# Day 90 - Search in Rotated Sorted Array II

## Problem

Given a rotated sorted array `nums` that may contain duplicate values,
return `true` if `target` is present in the array, otherwise return `false`.

### Example

Input:

nums = [2,5,6,0,0,1,2]
target = 0

Output:

true

## Approach

Use Binary Search.

- Set `left` and `right` pointers.
- Find the middle element.
- If `nums[mid] == target`, return `true`.
- If `nums[left] == nums[mid] == nums[right]`, duplicates make it
  impossible to identify the sorted half, so move both boundaries inward.
- Otherwise, determine which half is sorted.
- If the target lies inside the sorted half, search there.
- Otherwise, search the other half.
- Continue until the target is found or the search space becomes empty.

## Complexity

- Average Time Complexity: O(log n)
- Worst-case Time Complexity: O(n)
- Space Complexity: O(1)

Duplicates can cause the worst-case O(n) behavior.

## Platform

LeetCode #81 - Search in Rotated Sorted Array II
