# Day 53 - Clone Graph

## Problem

Given a reference to a node in a connected undirected graph, return a deep copy (clone) of the graph.

Each node contains an integer value and a list of its neighbors.

### Example

Input:

adjList = [[2,4],[1,3],[2,4],[1,3]]

Output:

[[2,4],[1,3],[2,4],[1,3]]

## Approach

- Use a Hash Map to store already cloned nodes.
- Perform DFS traversal starting from the given node.
- If the current node has already been cloned, return it.
- Otherwise:
  - Create a clone.
  - Store it in the Hash Map.
  - Recursively clone each neighbor.
- Return the cloned graph.

Each node is visited and cloned exactly once.

## Complexity

- Time Complexity: O(V + E)
- Space Complexity: O(V)

## Platform

LeetCode #133 - Clone Graph
