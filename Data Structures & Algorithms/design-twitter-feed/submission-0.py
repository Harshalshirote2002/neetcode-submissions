class Twitter:

    def __init__(self):
        self.user_posts_map = {}
        self.posts_counter = 0
        self.user_feed_map = {}
        self.user_followees_map = {}
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts_counter += 1
        if userId not in self.user_posts_map.keys():
            newList = []
            heapq.heapify(newList)
            heapq.heappush(newList, (-self.posts_counter, tweetId))
            self.user_posts_map[userId] = newList
        else:
            heapq.heappush(self.user_posts_map[userId], (-self.posts_counter, tweetId))
        

    def getNewsFeed(self, userId: int) -> list[int]:
        follows = self.user_followees_map.get(userId, [])
        print(userId, follows)
        follows.append(userId)
        posts = []
        heapq.heapify(posts)
        for flws in follows:
            flws_posts = self.user_posts_map.get(flws, [])
            for flws_post in flws_posts:
                heapq.heappush(posts, flws_post)

        self.user_followees_map[userId] = follows[:-1]

        top_10_posts = []
        while posts:
            order, tweetId = heapq.heappop(posts)
            top_10_posts.append(tweetId)
            if len(top_10_posts) == 10:
                return top_10_posts

        return top_10_posts



        
        

    def follow(self, followerId: int, followeeId: int) -> None:
        followees = self.user_followees_map.get(followerId)
        if followees:
            if followeeId not in followees:
                followees.append(followeeId)
                self.user_followees_map[followerId] = followees
        else:
            self.user_followees_map[followerId] = [followeeId]
         

    def unfollow(self, followerId: int, followeeId: int) -> None:
        followers = self.user_followees_map.get(followerId)
        if followers:
            if followeeId in followers:
                followers=[flw for flw in followers if flw!=followeeId]
                self.user_followees_map[followerId] = followers
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)