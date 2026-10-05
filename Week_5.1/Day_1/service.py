from factory import NotificationFactory

#service layer , code not knowing anything about the subclass
class ServiceNotification:
  
    def __init__(self, notifier_factory: NotificationFactory):
        self.notifier_factory = notifier_factory

    def send_notification(self, preferred_medium: str, receiptant: str , message :str) -> None:
        print(f"\n Service Layer : Notification updates logic running ")
        
        notifier = self.notifier_factory.get_medium(preferred_medium)
        
        notifier.send(
            receiptant=receiptant,
            message=message   
        )
        print("notification sent from send_notification")

