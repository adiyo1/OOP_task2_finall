
from User import User

class SocialNetwork:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
                cls._instance = super().__new__(cls)
                cls._instance._initialized = False
        return cls._instance

    def __init__(self, name):
        if self._initialized:
            return
        self.name = name
        self.network = {}
        self._users = {}
        print(f"The social network {self.name} was created!")
        #print("test1")
        self._initialized = True

    def __str__(self):
        usersstr = [str(self._users[username]) for username in self._users]  # List comprehension to get user info
        return f"{self.name} social network:\n" + "\n".join(usersstr) + "\n"




    def sign_up(self, username, password):        # Check if the user already exists
        if username in self._users:
            print(f"User {username} already exists. Please choose a different username.")
            return None
        if len(password) >8:
            print(f"Password {password} too long.")
            return None
        if len(password) <4:
            print(f"Password {password} too short.")
            return None
        # Create a new user and store it in the dictionary
        self.connect=True
        new_user = User(username, password)
        self._users[username] = new_user
        return new_user

    def log_out(self, username):
        # if self._users.get(username).connect==True:
            self.connect=False
            self._users[username].connect=False
            print(f"{username} disconnected")
        # else:
        #     print("already logged out")

    def log_in(self, username,password):
        if password==self._users[username].password:
            self.connect=True
            self._users[username].connect = True
            print(f"{username} connected")
        # if username in self._users: