# Day 83 - Rotate Image

## Problem

You are given an `n x n` 2D matrix representing an image.

Rotate the image by 90 degrees clockwise.

The rotation must be performed **in-place**, meaning the input matrix
must be modified directly without allocating another 2D matrix.

### Example

Input:

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

Output:

[[7,4,1],
 [8,5,2],
 [9,6,3]]

## Approach

The rotation can be achieved using two steps:

### Step 1: Transpose the Matrix

Swap elements across the main diagonal:

matrix[i][j] <-> matrix[j][i]

This converts:

1 2 3
4 5 6
7 8 9

into:

1 4 7
2 5 8
3 6 9

### Step 2: Reverse Every Row

Reverse each row:

1 4 7  ->  7 4 1
2 5 8  ->  8 5 2
3 6 9  ->  9 6 3

The resulting matrix is rotated 90 degrees clockwise.

## Complexity

- Time Complexity: O(n²)
- Space Complexity: O(1)

## Platform

LeetCode #48 - Rotate Image
