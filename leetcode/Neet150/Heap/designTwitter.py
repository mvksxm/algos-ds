from collections import defaultdict, deque
import heapq
from typing import List

# Approach
# 1) For each user create an ordered list of max len 10 for the posts associated with this user.
# 2) Create a max heap for the result. Iterate through the followees and add their top 10 recent posts to the max heap
# 3) Pop 10 first values from the max heap.
# 4) Return result.

# Improvement
# Space -> We can maintain a min heap of size 10 for the result, so that it does not grow up until (unique_users * 10).

# n = len(unique users)
# TC -> O(n * (log n * 10)) = O(n * log n)

# t - tweets; f - followees
# SC -> O(n * t) + O(n * f)

class Twitter:

    def __init__(self):
        self.user_db = defaultdict(dict) # followees; tweets ordered
        self.time = 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        user_data = self.user_db[userId]
        if not user_data.get("tweets"):
            tweets = deque([(tweetId, self.time)])
            user_data["tweets"] = tweets
            self.time += 1
            return

        if len(user_data["tweets"]) == 10:
            user_data["tweets"].popleft()

        user_data["tweets"].append((tweetId, self.time))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        user_data = self.user_db[userId]
        followees = user_data.get("followees")
        all_users = followees.copy() if followees else set()
        all_users.add(userId)

        news_heap = []
        for followee in all_users:
            followee_tweets = self.user_db[followee].get("tweets")
            if not followee_tweets: continue
            for tweet in followee_tweets:
                heapq.heappush_max(news_heap, (tweet[1], tweet[0]))

        news_feed = []
        count = 1
        while count <= 10 and news_heap:
            tweet_data = heapq.heappop_max(news_heap)
            news_feed.append(tweet_data[1])
            count += 1

        return news_feed

    def follow(self, followerId: int, followeeId: int) -> None:
        user_data = self.user_db[followerId]
        if not user_data.get("followees"):
            user_data["followees"] = {followeeId}
            return

        user_data["followees"].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        user_data = self.user_db[followerId]
        if not user_data.get("followees"): return
        user_data["followees"].remove(followeeId)

