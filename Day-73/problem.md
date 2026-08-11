# Day 73 - Burst Balloons

## Problem

You are given an array of balloons where each balloon has a number written
on it.

If the ith balloon is burst, you receive:

nums[i - 1] * nums[i] * nums[i + 1]

If i - 1 or i + 1 is outside the array, treat it as a balloon with value 1.

Return the maximum number of coins that can be collected by bursting all
the balloons in the best possible order.

### Example

Input:

nums = [3,1,5,8]

Output:

167

Explanation:

The balloons can be burst in the order:

[3,1,5,8]
→ [3,5,8]
→ [3,8]
→ [8]
→ []

Coins:

3 * 1 * 5
+ 3 * 5 * 8
+ 1 * 3 * 8
+ 1 * 8 * 1

= 167

## Approach

This problem is solved using Interval Dynamic Programming.

Instead of deciding which balloon to burst first, consider which balloon
will be burst last within an interval.

Add 1 to both ends of the array to handle the boundary cases.

For every interval `(left, right)`, try every balloon `k` between them
as the last balloon to burst.

The recurrence is:

dp[left][right] =
    max(
        dp[left][k]
        + nums[left] * nums[k] * nums[right]
        + dp[k][right]
    )

The left and right parts become independent after choosing the last
balloon.

## Complexity

- Time Complexity: O(n^3)
- Space Complexity: O(n^2)

## Platform

LeetCode #312 - Burst Balloons
