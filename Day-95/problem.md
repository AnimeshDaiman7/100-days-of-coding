# Day 95 - Word Ladder II

## Problem

Given two words `beginWord` and `endWord`, and a dictionary `wordList`,
return all the shortest transformation sequences from `beginWord` to
`endWord`.

A valid transformation sequence must satisfy:

- Every adjacent pair of words differs by exactly one letter.
- Every transformed word must exist in `wordList`.
- The final word must be `endWord`.

If no valid transformation exists, return an empty list.

### Example

Input:

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

Output:

[
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
]

## Approach

- Use Breadth-First Search (BFS) to explore the word graph level by level.
- Generate neighboring words by changing one character at a time.
- BFS guarantees that the first paths reaching `endWord` are the shortest.
- Store parent relationships for words reached at the shortest distance.
- After BFS finishes, use backtracking to construct all shortest paths.
- Return all valid shortest transformation sequences.

## Complexity

- Time Complexity: O(N × L²)
- Space Complexity: O(N × L)

Where `N` is the number of words and `L` is the length of each word.

## Platform

LeetCode #126 - Word Ladder II
