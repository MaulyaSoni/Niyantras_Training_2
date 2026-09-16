from factory import NotificationFactory

class OrderService:
  
    def __init__(self, notifier_factory: NotificationFactory):
        self.notifier_factory = notifier_factory

    def checkout_user(self, username: str, preferred_medium: str) -> None:
        print(f"\n Service Layer : Notification updates logic running ")
        
        notifier = self.notifier_factory.get_notification(preferred_medium)
        
        notifier.send(
            message="Your order has been processed Successfully", 
            sender=username
        )
        print("notification sent from checkout user")

