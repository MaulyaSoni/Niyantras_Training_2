from core import Notification
from notifiers import EmailNotifier , SMSNotifier , PushNotifier

class NotificationManager:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._cache = {}
        return cls._instance
    
    def get_notification(self , medium : str ) -> Notification:

        med = medium.strip().lower()
        if not med:
            raise ValueError(f"Invalid or unsupported medium : {medium}")   
        
        if med in self._cache:
            return self._cache[med]

        if med == "email":
            notifier = EmailNotifier()
        elif med == "push":
            notifier = PushNotifier()
        elif med == "sms":
            notifier = SMSNotifier()
        else:
            raise ValueError("Unknown notification") 
    
        self._cache[med] = notifier

        return notifier
