# Day 45 - Task Scheduler

## Problem

Given an array of CPU tasks represented by capital letters A to Z and a cooling interval `n`, return the minimum number of CPU intervals required to execute all tasks.

The same task cannot be executed again until at least `n` intervals have passed.

## Example

Input:
tasks = ["A","A","A","B","B","B"], n = 2

Output:
8

## Approach

1. Count the frequency of each task.
2. Find the highest occurring task.
3. Calculate the minimum schedule length using:

(maxFreq - 1) × (n + 1) + numberOfTasksWithMaxFrequency

4. The final answer is the maximum of:
   - Total number of tasks
   - Calculated schedule length

This greedy formula minimizes idle slots.

## Complexity

Time Complexity: O(n)

Space Complexity: O(1)

## Platform

LeetCode #621
