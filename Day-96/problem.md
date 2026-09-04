# Day 96 - Max Points on a Line

## Problem

Given an array of points where `points[i] = [xi, yi]` represents a point
on the X-Y plane, return the maximum number of points that lie on the
same straight line.

### Example

Input:

points = [[1,1],[2,2],[3,3]]

Output:

3

## Approach

- Consider every point as a reference point.
- Calculate the slope between the reference point and every other point.
- Use GCD to reduce the slope into a normalized `(dy, dx)` pair.
- Store the frequency of every slope in a hash map.
- The most frequent slope represents the largest group of points on
  the same line passing through the reference point.
- Update the global maximum after processing each reference point.

## Complexity

- Time Complexity: O(n² log n)
- Space Complexity: O(n)

## Platform

LeetCode #149 - Max Points on a Line
