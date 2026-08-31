# Day 92 - Human Traffic of Stadium

## Problem

We are given a `Stadium` table containing:

- `id`
- `visit_date`
- `people`

We need to display all records that are part of a sequence containing
three or more consecutive `id`s, where the number of people is greater
than or equal to `100` for every record.

The result should be ordered by `visit_date` in ascending order.

### Example

Input:

Stadium:
- id = 1, people = 10
- id = 2, people = 109
- id = 3, people = 150
- id = 4, people = 99
- id = 5, people = 145
- id = 6, people = 145
- id = 7, people = 145
- id = 8, people = 99

Output:

The records with ids 5, 6 and 7.

## Approach

- Use a self join on the `Stadium` table.
- Find three records with consecutive `id`s.
- Check that all three records have `people >= 100`.
- Return every record that belongs to a valid sequence.
- Use `DISTINCT` to avoid duplicate records when valid sequences overlap.
- Order the final result by `visit_date`.

## Complexity

- Time Complexity: O(n)
- Space Complexity: O(n)

## Platform

LeetCode #601 - Human Traffic of Stadium
