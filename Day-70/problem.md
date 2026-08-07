# Day 70 - Design Twitter

## Problem

Design a simplified version of Twitter.

Support the following operations:

- Post a tweet.
- Follow another user.
- Unfollow another user.
- Retrieve the 10 most recent tweet IDs in the user's news feed.

## Example

Input:

["Twitter","postTweet","getNewsFeed","follow","postTweet","getNewsFeed","unfollow","getNewsFeed"]

Output:

[null,null,[5],null,null,[6,5],null,[5]]

## Approach

- Store tweets for every user along with timestamps.
- Maintain a follow set for every user.
- While generating the news feed:
  - Push the latest tweet from each followed user into a Max Heap.
  - Repeatedly extract the newest tweet.
  - Add the previous tweet from the same user back into the heap.
- Stop after retrieving 10 tweets or when the heap becomes empty.

This avoids sorting every tweet and keeps retrieval efficient.

## Complexity

- postTweet: **O(1)**
- follow / unfollow: **O(1)**
- getNewsFeed: **O((F + 10) log F)**

Where:

- F = Number of followed users.

## Platform

LeetCode #355 - Design Twitter
