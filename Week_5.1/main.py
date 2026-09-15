# from logic import NotificationFactoryManager
# from notifications import checkout_user
# from security import check_medium 

# def main():

#     medium = str(input("Enter the medium of sending the message "))

#     # check_medium(medium)
    
#     checkout_user("MS", medium)

#     manager = NotificationManager()
#     sms1 = manager.get_notification("sms")
#     print(sms1)

# if __name__ == "__main__":  
#     main()



from factory import NotificationManager
from service import OrderService

def app():
 
    shared_factory = NotificationManager()
    
    # The rest remains exactly the same
    order_service = OrderService(notifier_factory=shared_factory)
    pref_med = str(input(" Enter the preferred medium : "))
    order_service.checkout_user(username ="MS",preferred_medium=pref_med)

if __name__ == "__main__":
    app()
























