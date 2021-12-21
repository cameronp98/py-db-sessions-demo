from datetime import datetime, timedelta


class Session:
    DEFAULT_LENGTH: timedelta = timedelta(seconds=3)

    def __init__(self, username, length: timedelta = DEFAULT_LENGTH):
        self.username = username
        self.created = datetime.now()
        self.length = length
        self.expires = self.created + length

    def is_expired(self) -> bool:
        """Returns True if the session has expired. """
        return self.expires <= datetime.now()

    def is_active(self) -> bool:
        """Returns True if the session has not expired. """
        return not self.is_expired()

    def __repr__(self):
        return f"Session(usn={self.username}, cre={self.created}, exp={self.expires}, act={self.is_active()})"
