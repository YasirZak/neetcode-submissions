class Twitter:

    def __init__(self):
        self.follow_map = {}
        self.posts = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.follow_map:
            self.follow_map[userId] = {userId}
        self.posts.append((tweetId,userId))

    def getNewsFeed(self, userId: int) -> List[int]:
        count = 0
        i = len(self.posts)-1
        res = []
        while count<10 and i>=0:
            if self.posts[i][1] in self.follow_map[userId]:
                count+=1
                res.append(self.posts[i][0])
            i-=1

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follow_map:
            self.follow_map[followerId] = {followerId}
        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId == followerId: return
        self.follow_map[followerId].discard(followeeId)
