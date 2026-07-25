# Day 57 - LRU Cache

## Problem

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the `LRUCache` class:

- `LRUCache(int capacity)` initializes the cache with a positive size.
- `get(key)` returns the value of the key if it exists; otherwise returns `-1`.
- `put(key, value)` inserts or updates the value. If the cache exceeds its capacity, evict the least recently used key.

Both operations must run in **O(1)** average time complexity.

### Example

Input:

["LRUCache","put","put","get","put","get","put","get","get","get"]

[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]

Output:

[null,null,null,1,null,-1,null,-1,3,4]

## Approach

- Store cache entries in a Hash Map.
- Maintain usage order using a Doubly Linked List.
- Move recently accessed nodes to the front.
- Remove the least recently used node from the tail when capacity is exceeded.

## Complexity

- Time Complexity: O(1) for both `get()` and `put()`
- Space Complexity: O(capacity)

## Platform

LeetCode #146 - LRU Cache
