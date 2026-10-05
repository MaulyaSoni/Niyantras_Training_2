from core import Notification
# concrete products , subclasses
class EmailNotifier(Notification):
    def send(self , message : str , receiptant : str):
        print(f"{message} from {receiptant} in form of email")

class SMSNotifier(Notification):
    def send(self , message : str , receiptant : str):
        print(f"{message} from {receiptant} in form of sms")
        
class PushNotifier(Notification):
    def send(self , message : str , receiptant : str):
        print(f"{message} from {receiptant} in form of push notification")
