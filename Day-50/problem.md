# 🎉 Day 50 - Decode Ways

## 🏆 Halfway Milestone: 50 Days of Coding!

Today marks **Day 50** of my #100DaysOfCode journey.

The challenge for today was **Decode Ways**, a classic Dynamic Programming problem that demonstrates how memoization and state transitions can dramatically optimize recursive solutions.

---

## Problem

A message containing letters from A-Z is encoded using:

1 -> A
2 -> B
...
26 -> Z

Given a string containing only digits, return the total number of ways to decode it.

If the string cannot be decoded, return 0.

### Example

Input:
s = "12"

Output:
2

Explanation:
"AB" (1,2)
"L" (12)

---

## Approach

- Use Dynamic Programming.
- Let `dp[i]` represent the number of ways to decode the substring starting at index `i`.
- If the current digit is not `'0'`, decode it as a single character.
- If the next two digits form a valid number between `10` and `26`, decode them together.
- Build the solution from right to left.

This avoids repeated computations and efficiently solves the problem.

---

## Complexity

- Time Complexity: O(n)
- Space Complexity: O(1)

---

## Platform

LeetCode #91 - Decode Ways
