from factory import NotificationFactory
from service import OrderService

def main():
 
    shared_factory = NotificationFactory()
    order_service = OrderService(notifier_factory=shared_factory)
    #providing service layer 
    pref_med = str(input(" Enter the preferred medium : "))
    order_service.checkout_user(username ="MS",preferred_medium=pref_med)

if __name__ == "__main__":
    main()
