from factory import NotificationManager

class OrderService:
  
    def __init__(self, notifier_factory: NotificationManager):
        self.notifier_factory = notifier_factory

    def checkout_user(self, username: str, preferred_medium: str) -> None:
        print(f"\n Service Layer : inventory and updates ")
        
        notifier = self.get_notifier(preferred_medium)
        
        notifier.send(
            message="Your order has been processed Successfully", 
            sender=username
        )

