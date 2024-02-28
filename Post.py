
from abc import ABC, abstractmethod

from matplotlib import pyplot as plt

import User


class Post(ABC):
    def __init__(self,name:User ,content, price=None, location= None, available= True):
        self.content = content
        self.name= name
        self.price = price
        self.location = location
        self.available = available
        self.likes= []
        self.comments = []
        self.observers= []
        self.my_notifications =[]
        name.notify_observer(f"{name.username} has a new post")

    def like(self, user:User):
         if user.connect:
            if self.name.username == user.username:
                if user not in self.likes:
                    self.likes.append(user)
                return
            else:
                if user not in self.likes:
                    self.likes.append(user)
                    self.notify_observers(f"{user.username} liked your post")
                    print(f"notification to {self.name.username}: {user.username} liked your post")
                return

    def comment(self, user:User, comment):
        if user.connect:
            if self.name.username == user.username:
                self.comments.append(user)
                return
            else:
                self.comments.append(user)
                self.notify_observers(f"{user.username} commented on your post")
                print(f"notification to {self.name.username}: {user.username} commented on your post: {comment}")

    def post(self, user:User, post):
        if user.connect:
            if self.name.username == user.username:
                return
            for follower in self._follows:
                self.post.append(user)
                self.notify_newpost(f"{self.username} has a new post")



    def notify_observers(self, notification):
        for observer in self.observers:
            observer.update(self, notification)
    def add_observer(self, observer):
        self.observers.append(observer)

    def display(self):
        print("Shows picture")

    def create_post(self, post_type,content,price,location,available):
        if self.connect:
            if post_type == "Text":
                newpost1 = (TextPost(self, content))
                newpost1.add_observer(self)
                return newpost1

            if post_type == "Image":
                newpost2 = (ImagePost(self, content))
                newpost2.add_observer(self)
                return newpost2
            if post_type == "Sale":
                newpost3 = (SalePost(self,content,price,location))
                newpost3.add_observer(self)
                return newpost3
            return ValueError("Invalid post type")






class TextPost(Post):
    def __init__(self, name: User, content):
        super().__init__(name,content)
        print(f"{name.username} published a post:")
        print(f'"{content}"\n')

    def __str__(self):
        return f'{self.name.username} published a post:\n"{self.content}"\n'



class ImagePost(Post):
    def __init__(self, name: User, content):
        super().__init__(name, content)
        print(f"{name.username} posted a picture\n")
    def display(self):
        image_rgb = plt.imread(self.content)
        plt.imshow(image_rgb)
        plt.axis('off')
        plt.show()
        print("Shows picture")

    def __str__(self):
        return f"{self.name.username} posted a picture\n"


class SalePost(Post):
    def __init__(self, name: User, content,price,location):
        super().__init__(name ,content,price,location)
        print(f"{name.username} posted a product for sale:")
        print(f"For sale! {content}, price: {price}, pickup from: {location}\n")
        #self.available= True

    def __str__(self):
        if self.available:
            avail = "For sale! "
        else:
            avail = "Sold! "
        return f"{self.name.username} posted a product for sale:\n{avail}{self.content}, price: {self.price}, pickup from: {self.location}\n"

    def discount(self, precent, password):
        if self.name.password== password:
           self.price= self.price- (self.price * precent/100)
           print(f"Discount on {self.name.username} product! the new price is: {self.price}")

    #@Override
    def print(Post):
        if(Post.post_type=="SalePost"):
            print(f"{Post.name.username} posted a product for sale:")
            if(Post.available==True):
                print(f"For Sale! {Post.content}")
            if(Post.available==False):
                print(f"Sold! {Post.content}")
    def sold(self, password):
        if self.name.password== password:
            self.available= False
            print(f"{self.name.username}'s product is sold")

