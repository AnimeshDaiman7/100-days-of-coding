# Day 54 - Rotting Oranges

## Problem

You are given an `m × n` grid where each cell can have one of three values:

- `0` representing an empty cell.
- `1` representing a fresh orange.
- `2` representing a rotten orange.

Every minute, any fresh orange that is **4-directionally adjacent** to a rotten orange becomes rotten.

Return the minimum number of minutes required until no cell has a fresh orange. If impossible, return `-1`.

### Example

Input:

grid =
[
 [2,1,1],
 [1,1,0],
 [0,1,1]
]

Output:

4

## Approach

- Traverse the grid once.
- Store all rotten oranges in a queue.
- Count the number of fresh oranges.
- Perform Multi-Source BFS.
- Each BFS level represents one minute.
- Infect adjacent fresh oranges and add them to the queue.
- If all fresh oranges become rotten, return the total minutes; otherwise return `-1`.

## Complexity

- Time Complexity: O(m × n)
- Space Complexity: O(m × n)

## Platform

LeetCode #994 - Rotting Oranges
