# Day 87 - Unique Binary Search Trees

## Problem

Given an integer `n`, return the number of structurally unique Binary
Search Trees (BSTs) which have exactly `n` nodes with unique values
from `1` to `n`.

### Example

Input:

n = 3

Output:

5

For `n = 3`, there are 5 structurally unique BSTs.

## Approach

Use Dynamic Programming.

- `dp[i]` represents the number of unique BSTs that can be formed using
  `i` nodes.
- Consider every node as the root.
- If `j` nodes are placed in the left subtree, then
  `i-j-1` nodes are placed in the right subtree.
- The number of trees for this root is:

  `dp[j] * dp[i-j-1]`

- Add the result for every possible root.

Base case:

`dp[0] = 1`

## Complexity

- Time Complexity: O(n²)
- Space Complexity: O(n)

## Platform

LeetCode #96 - Unique Binary Search Trees
