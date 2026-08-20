# Day 81 - Valid Number

## Problem

Given a string `s`, return whether `s` is a valid number.

A valid number can be:

1. An integer followed by an optional exponent.
2. A decimal number followed by an optional exponent.

An integer consists of an optional sign followed by one or more digits.

A decimal number can be:

- Digits followed by a dot.
- Digits followed by a dot followed by digits.
- A dot followed by digits.

An exponent is represented by `e` or `E` followed by an integer.

### Examples

Input:

s = "0"

Output:

true

Input:

s = "2e10"

Output:

true

Input:

s = "abc"

Output:

false

## Approach

The solution parses the string character by character.

We maintain two important states:

- Whether digits have appeared before the current position.
- Whether digits have appeared after the exponent.

We also track whether a decimal point or exponent has already been encountered.

### Rules

- A digit is always valid and updates the digit state.
- `+` or `-` is valid only at the beginning or immediately after `e/E`.
- `.` is valid only before an exponent and only once.
- `e/E` is valid only once and only if a digit has already appeared.
- After `e/E`, at least one digit must appear.
- Any other character makes the number invalid.

## Complexity

- Time Complexity: O(n)
- Space Complexity: O(1)

where `n` is the length of the string.

## Platform

LeetCode #65 - Valid Number
