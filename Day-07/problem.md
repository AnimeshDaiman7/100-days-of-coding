# Day 7 - Best Time to Buy and Sell Stock

## Problem

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve. If no profit can be made, return 0.

### Example

Input:
prices = [7,1,5,3,6,4]

Output:
5

Explanation:
Buy at price 1 and sell at price 6.

## Approach

- Keep track of the minimum price seen so far.
- For each day, calculate the profit if sold today.
- Update the maximum profit whenever a better profit is found.

## Complexity

- Time Complexity: O(n)
- Space Complexity: O(1)

## Platform

LeetCode #121 - Best Time to Buy and Sell Stock
