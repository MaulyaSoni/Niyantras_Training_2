from core import Notification

class EmailNotifier(Notification):
    def send(self , message : str , sender : str):
        print(f"sent the message from {sender} in form of email")

class SMSNotifier(Notification):
    def send(self , message : str , sender : str):
        print(f"sent the message from {sender} in form of sms")
        
class PushNotifier(Notification):
    def send(self , message : str , sender : str):
        print(f"sent the message from {sender} in form of push notification")
