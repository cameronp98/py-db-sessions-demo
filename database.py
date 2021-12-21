from typing import Optional, Union

from user import User
from session import Session


class Database:
    def __init__(self):
        self.users: dict[str, User] = {}

    def add_user(self, username, password) -> bool:
        """Add a new user with the given username and password.

        Returns False if a user already exists with the given username,
        Returns True if the user was created successfully.
        """
        if self.find_user(username) is not None:
            return False
        self.users[username] = (User(username, password))
        return True

    def find_user(self, username: str) -> Optional[User]:
        if username in self.users:
            return self.users[username]
        return None

    def login(self, username: str, password: str) -> bool:
        if (user := self.find_user(username)) is not None and user.password == password:
            # create a new session for this user that expires in 3 seconds
            user.sessions.append(Session(username))
            return True
        return False

    def has_logged_in_user(self, username: str) -> bool:
        """Returns True if the user with the given username has any active login sessions """
        return (user := self.find_user(username)) is not None and user.has_active_sessions()
