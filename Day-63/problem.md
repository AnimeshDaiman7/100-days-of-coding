# Day 63 - Word Search II

## Problem

Given an `m × n` board of characters and a list of strings `words`, return all words that can be found in the board.

A word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring.

The same letter cell may not be used more than once in a word.

### Example

Input:

board =
[
["o","a","a","n"],
["e","t","a","e"],
["i","h","k","r"],
["i","f","l","v"]
]

words = ["oath","pea","eat","rain"]

Output:

["eat","oath"]

## Approach

- Insert all words into a Trie.
- Start DFS from every cell.
- During DFS:
  - Follow Trie nodes matching board characters.
  - Stop immediately if the character doesn't exist in the Trie.
  - Add completed words to the answer.
- Use backtracking to restore visited cells.
- Mark found words to avoid duplicates.

## Complexity

- Time Complexity: O(M × N × 4ᴸ) (worst case)
- Space Complexity: O(total characters in Trie)

## Platform

LeetCode #212 - Word Search II
