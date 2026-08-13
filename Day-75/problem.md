# Day 75 - Largest Rectangle in Histogram

## Problem

Given an array of integers `heights` representing the histogram's bar height
where the width of each bar is `1`, return the area of the largest rectangle
in the histogram.

### Example

Input:

heights = [2,1,5,6,2,3]

Output:

10

Explanation:

The largest rectangle is formed using the bars with heights `5` and `6`.

The minimum height is `5` and the width is `2`.

Area = 5 * 2 = 10

## Approach

The solution uses a Monotonic Stack.

- Traverse the histogram from left to right.
- Store indices of bars in increasing height order.
- When the current bar is smaller than the bar at the top of the stack,
  the taller bar can no longer extend to the right.
- Remove the taller bar and calculate the largest rectangle using its height.
- The width is determined using the current index and the new top of the stack.
- Add a `0` at the end to process all remaining bars.

For every removed bar:

Area = height * width

Each index is pushed and popped from the stack at most once.

## Complexity

- Time Complexity: O(n)
- Space Complexity: O(n)

## Platform

LeetCode #84 - Largest Rectangle in Histogram
