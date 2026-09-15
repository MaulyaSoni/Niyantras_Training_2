from core import Notification

class EmailNotifier(Notification):
    def send(self , message : str , sender : str):
        print(f"sending the message from {sender} in form of email")

class SMSNotifier(Notification):
    def send(self , message : str , sender : str):
        print(f"sending the message from {sender} in form of sms")
        
class PushNotifier(Notification):
    def send(self , message : str , sender : str):
        print(f"sending the message from {sender} in form of push notification")
        
# class NotificationManager:

#     _instance = None

#     def __new__(cls):
#         if cls._instance is None:
#             cls._instance = super.__new__(cls)
#             cls._instance._cache = {}
#         return cls._instance
    
#     def get_notification(self , medium : str , message : str , sender : str) -> Notification:

#         med = medium.strip().lower()
#         if not nfs:
#             raise ValueError(f"Invalid or unsupported medium : {medium}")   
        
#         if med in self._cache:
#             return self._cache[med]

#         if med == "email":
#             notifier = EmailNotifier()
#         elif med == "push":
#             notifier = PushNotifier()
#         elif med == "sms":
#             notifier = SMSNotifier()
#         else:
#             raise ValueError("Unknown notification") 
    
#         self._cache[med] = notifier

#         return notifier
 