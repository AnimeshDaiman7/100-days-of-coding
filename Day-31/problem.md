# Day 31 - Valid Anagram

## 📝 Problem

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

An **anagram** is a word formed by rearranging the letters of another word using all the original letters exactly once.

---

## Example 1

Input:

s = "anagram"
t = "nagaram"

Output:

true

---

## Example 2

Input:

s = "rat"
t = "car"

Output:

false

---

## 💡 Approach

Use a **Hash Map (Dictionary)** to count the frequency of every character.

- Count characters in string `s`.
- Count characters in string `t`.
- If both frequency maps are identical, the strings are anagrams.
- Otherwise, they are not.

Python's `Counter` from the `collections` module makes this concise and efficient.

---

## ⏱ Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

*(At most 26 lowercase English letters.)*

---

## 🏷 Platform

LeetCode #242 - Valid Anagram
