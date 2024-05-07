from User import User
from Notification import INotification

class UserManager:
    def __init__(self, notifier):
        self.notifier = notifier
        self.users = {}

    def register_user(self, user: User):
        if user.user_type not in ["ocasional", "mayorista"]:
            raise ValueError("Invalid user type. Must be 'ocasional' or 'mayorista'")

        self.users[user.email] = user

        self.notifier.notify_registration(user)

        return user

    def update_user(self, email, **kwargs):
        if email not in self.users:
            raise ValueError("User not found")

        user = self.users[email]
        for key, value in kwargs.items():
            if hasattr(user, key):
                setattr(user, key, value)

        return user

    def delete_user(self, email):
        if email not in self.users:
            raise ValueError("User not found")

        del self.users[email]