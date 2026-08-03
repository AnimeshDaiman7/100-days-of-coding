# Day 66 - Edit Distance

## Problem

Given two strings `word1` and `word2`, return the minimum number of operations required to convert `word1` into `word2`.

Allowed operations:

- Insert a character
- Delete a character
- Replace a character

### Example

Input:

word1 = "horse"
word2 = "ros"

Output:

3

Explanation:

horse → rorse (replace 'h' with 'r')

rorse → rose (delete 'r')

rose → ros (delete 'e')

## Approach

- Create a DP table.
- Initialize the first row and first column.
- If characters match:
  - Copy the diagonal value.
- Otherwise:
  - Take the minimum of insert, delete, and replace operations.
- Return the value in the bottom-right cell.

## Complexity

- Time Complexity: O(m × n)
- Space Complexity: O(m × n)

Where:
- m = length of word1
- n = length of word2

## Platform

LeetCode #72 - Edit Distance
