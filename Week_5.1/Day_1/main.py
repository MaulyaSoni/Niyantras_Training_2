from factory import NotificationFactory
from service import ServiceNotification

def main():
 
    factory = NotificationFactory()
    notification = ServiceNotification(notifier_factory=factory)

    pref_med = str(input("Enter the preferred medium : "))
    receiptant = str(input("Enter the receiptant name : "))
    message = str(input("Enter message :"))
    
    notification.send_notification(pref_med , receiptant , message)

if __name__ == "__main__":
    main()
