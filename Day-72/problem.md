# Day 72 - Maximum Profit in Job Scheduling

## Problem

We have `n` jobs where every job is scheduled from `startTime[i]` to
`endTime[i]`, obtaining a profit of `profit[i]`.

Return the maximum profit that can be obtained such that no two selected
jobs have overlapping time ranges.

If one job ends at time `x`, another job starting at time `x` can be selected.

### Example

Input:

startTime = [1,2,3,3]
endTime = [3,4,5,6]
profit = [50,10,40,70]

Output:

120

## Approach

- Combine the start time, end time and profit of every job.
- Sort the jobs by their ending time.
- Use Dynamic Programming to store the maximum profit achievable up to each job.
- For every job:
  - Find the latest previous job whose end time is less than or equal to
    the current job's start time.
  - Calculate the profit if the current job is selected.
  - Compare it with the profit obtained by skipping the current job.
- Binary Search is used to find the compatible previous job efficiently.

## Complexity

- Time Complexity: O(n log n)
- Space Complexity: O(n)

## Platform

LeetCode #1235 - Maximum Profit in Job Scheduling
