# Day 58 - Coin Change

## Problem

You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.

Return the fewest number of coins needed to make up that amount.

If the amount cannot be made up by any combination of the coins, return `-1`.

You may assume that you have an infinite number of each kind of coin.

### Example

Input:

coins = [1,2,5]

amount = 11

Output:

3

Explanation:

11 = 5 + 5 + 1

## Approach

- Create a DP array where `dp[i]` stores the minimum coins needed for amount `i`.
- Initialize all values to infinity except `dp[0] = 0`.
- For every amount:
  - Try every coin.
  - Update the minimum coins if using that coin leads to a better solution.
- Return `dp[amount]` if possible; otherwise return `-1`.

## Complexity

- Time Complexity: O(amount × number_of_coins)
- Space Complexity: O(amount)

## Platform

LeetCode #322 - Coin Change
