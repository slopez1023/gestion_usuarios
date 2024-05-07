from Notification import INotification

class EmailNotifier(INotification):
    def notify_registration(self, user):
        print(f"Sending welcome email to {user.email}")

        