# Day 43 - Best Time to Buy and Sell Stock II

## Problem

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

You may buy and/or sell the stock multiple times, but you can only hold one share at a time.

Return the maximum profit you can achieve.

### Example

Input:
prices = [7,1,5,3,6,4]

Output:
7

## Approach

- Traverse the prices array once.
- Whenever today's price is greater than yesterday's,
  add the profit.
- Repeat until the end.

This greedy strategy captures every profitable transaction.

## Complexity

- Time Complexity: O(n)
- Space Complexity: O(1)

## Platform

LeetCode #122 - Best Time to Buy and Sell Stock II
