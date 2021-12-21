from session import Session


class User:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        self.sessions = []

    def __repr__(self):
        return f"User(usn={self.username}, ses={self.sessions})"

    def add_session(self, session: Session):
        self.sessions.append(session)

    def has_active_sessions(self):
        return any(s.is_active() for s in self.sessions)
