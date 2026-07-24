# Day 56 - Course Schedule

## Problem

There are `numCourses` courses labeled from `0` to `numCourses - 1`.

You are given an array `prerequisites` where `prerequisites[i] = [a, b]` indicates that you must first take course `b` before taking course `a`.

Return `true` if you can finish all courses. Otherwise, return `false`.

### Example

Input:

numCourses = 2

prerequisites = [[1,0]]

Output:

true

### Example 2

Input:

numCourses = 2

prerequisites = [[1,0],[0,1]]

Output:

false

## Approach

- Build an adjacency list.
- Perform DFS on every course.
- Maintain a recursion stack (`visiting`) to detect cycles.
- If a node is visited again while still in the recursion stack, a cycle exists.
- Remove processed nodes from the graph to avoid repeated work.

## Complexity

- Time Complexity: O(V + E)
- Space Complexity: O(V + E)

## Platform

LeetCode #207 - Course Schedule
