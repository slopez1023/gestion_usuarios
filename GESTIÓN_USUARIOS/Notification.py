from abc import ABC, abstractmethod


class INotification:
    @abstractmethod
    def notify_registration(self, user):
        pass