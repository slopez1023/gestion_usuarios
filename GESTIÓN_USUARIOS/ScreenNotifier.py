from Notification import INotification

class ScreenNotifier(INotification):
    def notify_registration(self, user):
        if user.user_type == "ocasional":
            print("You have been registered successfully. You will soon have access to our web catalog of technology products.")
        else:
            print("You have been registered successfully.")