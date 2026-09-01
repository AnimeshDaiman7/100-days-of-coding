# Day 93 - Best Time to Buy and Sell Stock III

## Problem

You are given an array `prices` where `prices[i]` is the price of a stock
on the `i`th day.

Find the maximum profit you can achieve using at most two transactions.

You cannot hold multiple transactions at the same time. You must sell the
stock before buying again.

### Example

Input:

prices = [3,3,5,0,0,3,1,4]

Output:

6

Explanation:

Buy on day 4 at price 0 and sell on day 6 at price 3.

Profit = 3 - 0 = 3

Then buy on day 7 at price 1 and sell on day 8 at price 4.

Profit = 4 - 1 = 3

Total profit = 3 + 3 = 6

## Approach

Use Dynamic Programming with four states:

- `buy1` = maximum profit after the first buy.
- `sell1` = maximum profit after the first sell.
- `buy2` = maximum profit after the second buy.
- `sell2` = maximum profit after the second sell.

For every price:

- Update the first buy.
- Update the first sell.
- Update the second buy using the first transaction's profit.
- Update the second sell using the second transaction's profit.

The answer is the maximum profit after completing at most two
transactions.

## Complexity

- Time Complexity: O(n)
- Space Complexity: O(1)

## Platform

LeetCode #123 - Best Time to Buy and Sell Stock III
