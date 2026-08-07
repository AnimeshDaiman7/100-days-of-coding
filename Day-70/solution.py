from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweetMap[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int):
        res = []
        heap = []

        self.followMap[userId].add(userId)

        for followee in self.followMap[userId]:
            tweets = self.tweetMap[followee]
            if tweets:
                idx = len(tweets) - 1
                time, tweet = tweets[idx]
                heapq.heappush(heap, (-time, tweet, followee, idx - 1))

        while heap and len(res) < 10:
            _, tweet, followee, idx = heapq.heappop(heap)
            res.append(tweet)

            if idx >= 0:
                time, nxt = self.tweetMap[followee][idx]
                heapq.heappush(heap, (-time, nxt, followee, idx - 1))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId] and followeeId != followerId:
            self.followMap[followerId].remove(followeeId)
