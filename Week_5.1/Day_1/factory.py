from core import Notification
from notifiers import EmailNotifier , SMSNotifier , PushNotifier
from typing import Dict
#Creator Factory
class NotificationFactory:

    _instance = None
    _cache : Dict[str , Notification] = {}
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(NotificationFactory , cls).__new__(cls)
            cls._instance._classes = {
                "sms":SMSNotifier,
                "email":EmailNotifier,
                "push":PushNotifier
            }
            cls._instance._cache = {}

        return cls._instance
    
    def get_medium(self , medium : str ) -> Notification:

        med = medium.lower()
        
        if med not in self._cache:
            sender_cls= self._classes.get(med)
            if not sender_cls:
                raise ValueError(f"{med} , Unsupported medium for sending notifications")

            # Lazy init
            print(f"Cache miss{sender_cls}, Creating new instance for cache ")
            self._cache[med] = sender_cls()

        else:
            print(f"Cache hit , reusing the {med} for process")
        
        return self._cache[med]
