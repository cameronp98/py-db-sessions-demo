import time

from database import Database


def main():
    database = Database()
    database.add_user("bob", "nuggets")
    if database.login("bob", "nuggets"):
        print("Bob sessions after login:", database.users["bob"].sessions)
        assert database.has_logged_in_user("bob")

    time.sleep(4)

    print("Bob sessions after 4s:", database.users["bob"].sessions)

    assert database.has_logged_in_user("bob") == False


if __name__ == "__main__":
    main()
