from Post import Post, TextPost, ImagePost, SalePost
from abc import ABCMeta, abstractmethod


class User:

    def __init__(self, username, password):

        self.username = username
        self.password = password
        self._follows = []
        self._likes = []
        self.observers= []
        self.connect= True
        self.num_posts = 0
        self.posts = []
        self.my_notification = []
        self.num_followers = 0



    def __str__(self):
        return (f"User name: {self.username}, Number of posts: {self.num_posts}, Number of followers: {self.num_followers}")
    def update(self, observable, notification):
        self.my_notification.append(notification)

    def notify_observer(self, notification):
        for observer in self.observers:
            observer.update(self, notification)


    def print_notifications(self):
        print(f"{self.username}'s notifications:")
        for notification in self.my_notification:
            print(f"{notification}")

        # Call the function to print notifications
        # print_notifications()



    def notify_followers(self, post):
        for follower in self._follows:
            print(f"Notification to {follower.username}: {self.username} published a {post.__class__.__name__}")

    def notify_likes(self, liker, post):
        print(f"Notification to {self.username}: {liker.username} liked your post")
    def notify_comments(self, comment, post):
        print(f"Notification to {self.username}: {comment.username}commented your post")

    def notify_newpost(self, post):
        print(f"{self.username} has a new post")


    def unfollow(self,username):
        if self.connect:
            if self in username._follows:
                username._follows.remove(self)
                username.num_followers -=1
                #self.my_notification.remove(username)
                print(f"{self.username} unfollowed {username.username}")


    def follow(self, fusername):
        if self.connect:
            newf = fusername.username
            if self in fusername._follows:
                print(f"User '{newf}' is already being followed.")
                return None

            # Create a new user and store it in the dictionary
            else:
                fusername._follows.append(self)
                #self._follows.append(fusername)
                fusername.num_followers +=1
                print(f"{self.username} started following {newf}")
                return None



    def publish_post(self, post_type, content,price=None,location=None, available= True):
        if self.connect:
            self.num_posts += 1

            for follower in self._follows:
                follower.my_notification.append(f"{self.username} has a new post")

            return Post.create_post(self, post_type, content, price,location, available=True)






